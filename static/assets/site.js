(function(){
  // Banner e consenso: /assets/consent.js (componente unico). gtag esiste sempre ma Analytics si carica solo dopo "Accetta":
  // senza consenso gli eventi restano in coda nella pagina e non partono.
  // In più, ogni clic su Prenota direttamente, Airbnb, Booking.com, WhatsApp, telefono o email va al contatore anonimo (worker/ev.js):
  // niente cookie e niente dati personali (solo evento, pagina e lingua), quindi conta anche chi rifiuta i cookie.
  var EV='https://trullo-ev.cfdist2.workers.dev/ev';
  document.addEventListener('click',function(ev){
    var a=ev.target.closest&&ev.target.closest('a');if(!a)return;var h=a.href||'';
    var direct=a.getAttribute('data-ev')==='prenota_diretto';
    var kind=direct?'diretto':h.indexOf('wa.me')>-1?'whatsapp':h.indexOf('tel:')===0?'telefono':h.indexOf('mailto:')===0?'email':h.indexOf('airbnb.')>-1?'airbnb':h.indexOf('booking.com')>-1?'booking':null;
    var name={diretto:'prenota_diretto',whatsapp:'contatto_whatsapp',telefono:'contatto_telefono',email:'contatto_email',airbnb:'prenota_airbnb',booking:'prenota_booking'}[kind];
    if(!name)return;
    try{
      var box=a.closest('.book-box,.cta,footer,header,nav');
      var body=JSON.stringify({e:name,p:location.pathname,l:document.documentElement.lang||'',s:box?(box.tagName==='FOOTER'?'footer':box.tagName==='HEADER'||box.tagName==='NAV'?'header':'box'):'testo'});
      if(navigator.sendBeacon)navigator.sendBeacon(EV,new Blob([body],{type:'text/plain'}));
      else fetch(EV,{method:'POST',body:body,keepalive:true,mode:'no-cors'});
    }catch(e){}
    if(window.gtag)gtag('event',name,{metodo:kind,link_url:h});
  });

  // Modulo "Prenota direttamente" (14/11/2026): niente dati al sito, prepara WhatsApp o email con date e ospiti.
  // Evento richiesta_diretta (contatore anonimo + GA4 se c'è consenso), con il canale scelto.
  function send(name,s){
    try{
      var body=JSON.stringify({e:name,p:location.pathname,l:document.documentElement.lang||'',s:s});
      if(navigator.sendBeacon)navigator.sendBeacon(EV,new Blob([body],{type:'text/plain'}));
      else fetch(EV,{method:'POST',body:body,keepalive:true,mode:'no-cors'});
    }catch(e){}
  }
  function fmt(v){var p=(v||'').split('-');return p.length===3?p[2]+'/'+p[1]+'/'+p[0]:v;}
  var today=new Date(Date.now()-new Date().getTimezoneOffset()*6e4).toISOString().slice(0,10);
  Array.prototype.forEach.call(document.querySelectorAll('form.direct-form'),function(f){
    var ci=f.elements.arrivo,co=f.elements.partenza,err=f.querySelector('.df-err');
    ci.min=today;co.min=today;
    ci.addEventListener('change',function(){if(ci.value){co.min=ci.value;if(co.value&&co.value<=ci.value)co.value='';}});
    f.addEventListener('submit',function(ev){
      ev.preventDefault();
      var via=(ev.submitter&&ev.submitter.value)||'whatsapp';
      if(!ci.value||!co.value||co.value<=ci.value){err.textContent=f.getAttribute('data-err');err.hidden=false;return;}
      err.hidden=true;
      var d={ci:fmt(ci.value),co:fmt(co.value),n:f.elements.ospiti.value,nome:(f.elements.nome.value||'').trim(),msg:(f.elements.messaggio.value||'').trim()};
      var r=function(t){return t.replace(/\{(\w+)\}/g,function(_,k){return d[k]||'';});};
      var text=r(f.getAttribute('data-tpl'));
      if(d.msg)text+='\n\n'+d.msg;
      if(d.nome)text+='\n\n'+r(f.getAttribute('data-sign'));
      send('richiesta_diretta',via);
      if(window.gtag)gtag('event','richiesta_diretta',{metodo:via,arrivo:ci.value,notti:Math.round((new Date(co.value)-new Date(ci.value))/864e5),ospiti:+d.n});
      if(via==='email'){
        location.href='mailto:'+f.getAttribute('data-email')+'?subject='+encodeURIComponent(r(f.getAttribute('data-subject')))+'&body='+encodeURIComponent(text);
      }else{
        var u=f.getAttribute('data-wa')+'?text='+encodeURIComponent(text);
        if(!window.open(u,'_blank','noopener'))location.href=u;
      }
    });
  });
})();
