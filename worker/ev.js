// Trullo Rosy – contatore anonimo dei clic su Prenota direttamente (e invii del modulo), Airbnb, Booking.com, WhatsApp, telefono ed email.
// Cloudflare Worker "trullo-ev" (https://trullo-ev.cfdist2.workers.dev), stesso schema di ev.php di RAM.
// Non usa cookie e non salva IP, user agent o altri dati personali: solo minuto, evento, pagina e lingua.
// Binding (impostato su Cloudflare, mai nel repository):
//   DB  D1 "trullo-events"  tabella events (ts, e, p, l, s, v)
// POST /ev        {"e":"prenota_airbnb","p":"/it/guide/…","l":"it"}  → 204
// GET  /ev-stats  ?days=35  → {"since":"AAAA-MM-GG","rows":[{day,e,p,l,s,n,v}]}
// GET  /avail     → {"busy":[["AAAA-MM-GG","AAAA-MM-GG"],…],"updated":"…"}  notti occupate [arrivo, partenza)
//   Legge i calendari iCal di Airbnb e Booking.com (secret ICAL_AIRBNB e ICAL_BOOKING, mai nel repository).
//   Il calendario Airbnb importa già Booking, Vrbo e atraveo: basta lui, Booking è una sicurezza in più.
//   Risponde solo con le date occupate (niente nomi o dettagli delle prenotazioni), cache 30 minuti.

const EVENTS = ['prenota_diretto', 'richiesta_diretta', 'prenota_airbnb', 'prenota_booking', 'contatto_whatsapp', 'contatto_telefono', 'contatto_email'];
const ORIGINS = ['https://trullo-rosy.it', 'https://www.trullo-rosy.it'];

function cors(req) {
  const o = req.headers.get('Origin') || '';
  return ORIGINS.includes(o) ? { 'Access-Control-Allow-Origin': o, 'Vary': 'Origin' } : {};
}

async function ev(req, env, ctx) {
  const none = new Response(null, { status: 204, headers: { 'Cache-Control': 'no-store', ...cors(req) } });
  if (req.method !== 'POST' || !env.DB) return none;
  if (/bot|crawl|spider|slurp|headless|lighthouse|preview/i.test(req.headers.get('User-Agent') || '')) return none;
  const o = req.headers.get('Origin');
  if (o && !ORIGINS.includes(o)) return none;
  let j;
  try { j = JSON.parse((await req.text()).slice(0, 2000)); } catch { return none; }
  if (!j || !EVENTS.includes(j.e)) return none;
  const clean = (v, n) => String(v ?? '').replace(/[^A-Za-z0-9/\-_.:%]/g, '').slice(0, n);
  const p = clean(j.p, 160);
  if (!p.startsWith('/')) return none;
  const ts = new Date().toISOString().slice(0, 16).replace('T', ' ');
  ctx.waitUntil(env.DB.prepare('INSERT INTO events (ts, e, p, l, s, v) VALUES (?, ?, ?, ?, ?, ?)')
    .bind(ts, j.e, p, clean(j.l, 8), clean(j.s, 40), 0).run().catch(() => {}));
  return none;
}

function icalBusy(txt) {
  const out = [];
  const t = txt.replace(/\r?\n[ \t]/g, '');
  for (const ev of t.split('BEGIN:VEVENT').slice(1)) {
    const g = k => { const m = ev.match(new RegExp('^' + k + '[^:\\r\\n]*:(\\d{8})', 'm')); return m ? m[1].replace(/(\d{4})(\d{2})(\d{2})/, '$1-$2-$3') : null; };
    const a = g('DTSTART'), b = g('DTEND');
    if (a && b && b > a) out.push([a, b]);
  }
  return out;
}

async function avail(req, env, ctx) {
  const h = { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'public, max-age=1800', 'X-Robots-Tag': 'noindex', ...cors(req) };
  const cache = caches.default;
  const key = new Request('https://trullo-ev.internal/avail');
  let hit = await cache.match(key);
  if (!hit) {
    const today = new Date().toISOString().slice(0, 10);
    let all = [], ok = 0;
    for (const u of [env.ICAL_AIRBNB, env.ICAL_BOOKING].filter(Boolean)) {
      try {
        const r = await fetch(u, { headers: { 'User-Agent': 'trullo-rosy.it calendar sync' }, cf: { cacheTtl: 900 } });
        if (r.ok) { all = all.concat(icalBusy(await r.text())); ok++; }
      } catch {}
    }
    all = all.filter(([, b]) => b > today).sort((x, y) => x[0] < y[0] ? -1 : 1);
    const busy = [];
    for (const [a, b] of all) {
      const last = busy[busy.length - 1];
      if (last && a <= last[1]) { if (b > last[1]) last[1] = b; } else busy.push([a, b]);
    }
    hit = new Response(JSON.stringify({ busy, sources: ok, updated: new Date().toISOString() }), { headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'public, max-age=1800' } });
    if (ok) ctx.waitUntil(cache.put(key, hit.clone()));
  }
  return new Response(await hit.text(), { headers: h });
}

async function evStats(url, env) {
  const h = { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex' };
  const days = Math.max(1, Math.min(120, parseInt(url.searchParams.get('days') || '35', 10) || 35));
  const since = new Date(Date.now() - days * 864e5).toISOString().slice(0, 10);
  const { results } = await env.DB.prepare(
    'SELECT substr(ts,1,10) AS day, e, p, l, s, COUNT(*) AS n, SUM(v) AS v FROM events WHERE ts >= ? GROUP BY day, e, p, l, s'
  ).bind(since).all();
  return new Response(JSON.stringify({ since, rows: results }), { headers: h });
}

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    if (req.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: { ...cors(req), 'Access-Control-Allow-Methods': 'GET, POST', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '86400' } });
    }
    if (url.pathname === '/ev') return ev(req, env, ctx);
    if (url.pathname === '/ev-stats') return evStats(url, env);
    if (url.pathname === '/avail') return avail(req, env, ctx);
    return new Response('Not found', { status: 404, headers: { 'X-Robots-Tag': 'noindex' } });
  }
};
