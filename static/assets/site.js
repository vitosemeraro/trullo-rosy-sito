(function(){
  // Banner e consenso: /assets/consent.js (componente unico). gtag esiste sempre ma Analytics si carica solo dopo "Accetta":
  // senza consenso gli eventi restano in coda nella pagina e non partono.
  document.addEventListener('click',function(ev){
    if(!window.gtag)return;
    var a=ev.target.closest&&ev.target.closest('a');if(!a)return;var h=a.href||'';
    var kind=h.indexOf('wa.me')>-1?'whatsapp':h.indexOf('tel:')===0?'telefono':h.indexOf('mailto:')===0?'email':h.indexOf('airbnb.')>-1?'airbnb':h.indexOf('booking.com')>-1?'booking':null;
    var name={whatsapp:'contatto_whatsapp',telefono:'contatto_telefono',email:'contatto_email',airbnb:'prenota_airbnb',booking:'prenota_booking'}[kind];
    if(name)gtag('event',name,{metodo:kind,link_url:h});
  });
})();
