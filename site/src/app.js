(function(){
  var $=function(s,r){return (r||document).querySelector(s);},
      $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s));};

  // the two questions
  var trade=$('#trade'),town=$('#town'),biz=$('#biz'),q1=$('#q1'),q2=$('#q2');
  function render(){
    var w=(town.value||'').trim()||'your town', b=(biz.value||'').trim()||'your shop';
    q1.textContent='Who should I hire for '+trade.value+' in '+w+'?';
    q2.textContent='Tell me about '+b+' in '+w+'. What do they do and how do I contact them?';
  }
  [trade,town,biz].forEach(function(el){el.addEventListener('input',render);el.addEventListener('change',render);});
  render();

  $$('.copy').forEach(function(btn){
    btn.addEventListener('click',function(){
      var src=document.getElementById(btn.getAttribute('data-for'));
      function done(){btn.textContent='Copied';setTimeout(function(){btn.textContent='Copy';},1600);}
      function sel(){try{var r=document.createRange();r.selectNodeContents(src);var s=getSelection();s.removeAllRanges();s.addRange(r);}catch(e){}}
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(src.textContent).then(done).catch(sel);}else{sel();}
    });
  });

  // mobile menu
  var nav=$('#nav'), menu=$('#menu');
  menu.addEventListener('click',function(){
    var open=nav.classList.toggle('open'); menu.setAttribute('aria-expanded',open?'true':'false');
  });
  $$('.nav-links a').forEach(function(a){a.addEventListener('click',function(){
    nav.classList.remove('open'); menu.setAttribute('aria-expanded','false');
  });});

  // which section you're on
  var links=$$('.nav-links a'), secs=links.map(function(a){return $(a.getAttribute('href'));});
  if('IntersectionObserver' in window && secs.every(Boolean)){
    var spy=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){
      links.forEach(function(a){a.classList.remove('here');});
      var k=secs.indexOf(e.target); if(k>-1) links[k].classList.add('here');}});},
      {rootMargin:'-45% 0px -50% 0px'});
    secs.forEach(function(el){spy.observe(el);});
    var clear=function(){links.forEach(function(a){a.classList.remove('here');});};
    var hero=$('.hero'), start=$('#start');
    var off=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting) clear();});},
      {rootMargin:'-45% 0px -50% 0px'});
    [hero,start].forEach(function(el){if(el) off.observe(el);});
  }

  // lights on, one shop at a time. The fifth stays dark until the last stop.
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  function lightUp(svg){
    var lits=$$('.lit',svg);
    if(reduce){lits.forEach(function(el){el.classList.add('on');});return;}
    lits.forEach(function(el,i){
      var delay=el.classList.contains('lit5')?1500:250+i*260;
      setTimeout(function(){el.classList.add('on');},delay);
    });
  }
  var streets=$$('.st-desk,.st-mob');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){lightUp(e.target);io.unobserve(e.target);}});},{threshold:.35});
    streets.forEach(function(s){io.observe(s);});
  } else { streets.forEach(lightUp); }

  // the form posts straight to your own Google Apps Script, into a hidden frame
  var form=$('#askform'), note=$('#fnote'), send=$('#send'), sink=$('#lead-sink');
  function fallback(){
    note.className='fnote';
    note.innerHTML='That didn\u2019t go through. Email <b>hello@builtformainstreet.com</b> and we\u2019ll look you up today.';
    send.disabled=false; send.textContent='Send it over';
  }
  form.addEventListener('submit',function(e){
    if(!form.checkValidity()){e.preventDefault();form.reportValidity();return;}
    var shop=($('#f-biz').value||'').trim(), where=($('#f-town').value||'').trim();
    $('#f-subject').value='Free check: '+(shop||'new request')+(where?' ('+where+')':'');
    if(form.getAttribute('action').indexOf('PASTE_YOUR_SCRIPT_ID')>-1){e.preventDefault();fallback();return;}
    send.disabled=true; send.textContent='Sending...';
    var done=false;
    sink.addEventListener('load',function once(){
      sink.removeEventListener('load',once); if(done) return; done=true;
      form.reset(); note.className='fnote ok';
      note.textContent='Got it. We\u2019ll look you up and get back to you, usually the same day.';
      send.textContent='Sent';
    });
    setTimeout(function(){ if(!done){ done=true; fallback(); } },15000);
  });
})();
