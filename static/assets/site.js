(function(){
  var KEY='tr_consent';
  function get(){try{return localStorage.getItem(KEY)}catch(e){return null}}
  function set(v){try{localStorage.setItem(KEY,v)}catch(e){}}
  function loadGA(){
    if(window.__ga||!window.GA4)return;window.__ga=1;
    var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id='+window.GA4;document.head.appendChild(s);
    window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};
    gtag('js',new Date());gtag('config',window.GA4,{anonymize_ip:true});
    document.addEventListener('click',function(ev){
      var a=ev.target.closest&&ev.target.closest('a');if(!a)return;var h=a.href||'';
      var kind=h.indexOf('wa.me')>-1?'whatsapp':h.indexOf('tel:')===0?'telefono':h.indexOf('mailto:')===0?'email':h.indexOf('airbnb.')>-1?'airbnb':h.indexOf('booking.com')>-1?'booking':null;
      var name={whatsapp:'contatto_whatsapp',telefono:'contatto_telefono',email:'contatto_email',airbnb:'prenota_airbnb',booking:'prenota_booking'}[kind];
      if(name)gtag('event',name,{metodo:kind,link_url:h});
    });
  }
  var box=document.getElementById('cookie');
  var c=get();
  if(c==='granted')loadGA();else if(!c&&box)box.hidden=false;
  document.addEventListener('click',function(ev){
    var b=ev.target.closest&&ev.target.closest('[data-consent]');
    if(b){set(b.getAttribute('data-consent'));box.hidden=true;if(b.getAttribute('data-consent')==='granted')loadGA();}
    if(ev.target.closest&&ev.target.closest('[data-reset-consent]')){try{localStorage.removeItem(KEY)}catch(e){}box.hidden=false;}
    var sb=ev.target.closest&&ev.target.closest('[data-cookie-settings]');
    if(sb){var pn=box.querySelector('.cookie-panel');pn.hidden=!pn.hidden;sb.setAttribute('aria-expanded',String(!pn.hidden));box.querySelector('[data-cookie-stat]').checked=get()==='granted';}
    if(ev.target.closest&&ev.target.closest('[data-cookie-save]')){var on=box.querySelector('[data-cookie-stat]').checked;set(on?'granted':'denied');box.hidden=true;if(on)loadGA();}
  });
})();
