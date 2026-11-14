(function(){
  // Banner e consenso: /assets/consent.js (componente unico). gtag esiste sempre ma Analytics si carica solo dopo "Accetta":
  // senza consenso gli eventi restano in coda nella pagina e non partono.
  // In più, ogni clic su Airbnb, Booking.com, WhatsApp, telefono o email va al contatore anonimo (worker/ev.js):
  // niente cookie e niente dati personali (solo evento, pagina e lingua), quindi conta anche chi rifiuta i cookie.
  var EV='https://trullo-ev.cfdist2.workers.dev/ev';
  document.addEventListener('click',function(ev){
    var a=ev.target.closest&&ev.target.closest('a');if(!a)return;var h=a.href||'';
    var kind=h.indexOf('wa.me')>-1?'whatsapp':h.indexOf('tel:')===0?'telefono':h.indexOf('mailto:')===0?'email':h.indexOf('airbnb.')>-1?'airbnb':h.indexOf('booking.com')>-1?'booking':null;
    var name={whatsapp:'contatto_whatsapp',telefono:'contatto_telefono',email:'contatto_email',airbnb:'prenota_airbnb',booking:'prenota_booking'}[kind];
    if(!name)return;
    try{
      var box=a.closest('.book-box,.cta,footer,header,nav');
      var body=JSON.stringify({e:name,p:location.pathname,l:document.documentElement.lang||'',s:box?(box.tagName==='FOOTER'?'footer':box.tagName==='HEADER'||box.tagName==='NAV'?'header':'box'):'testo'});
      if(navigator.sendBeacon)navigator.sendBeacon(EV,new Blob([body],{type:'text/plain'}));
      else fetch(EV,{method:'POST',body:body,keepalive:true,mode:'no-cors'});
    }catch(e){}
    if(window.gtag)gtag('event',name,{metodo:kind,link_url:h});
  });
})();
