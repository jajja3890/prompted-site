(()=>{
const toggle=document.querySelector('.nav-toggle');const nav=document.querySelector('.mobile-nav');if(toggle&&nav){toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?(document.documentElement.lang==='en'?'Close menu':'Sulje valikko'):(document.documentElement.lang==='en'?'Open menu':'Avaa valikko'));nav.setAttribute('aria-hidden',String(!open));});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label',document.documentElement.lang==='en'?'Open menu':'Avaa valikko');nav.setAttribute('aria-hidden','true');}));}

// Keyboard dismissal of the mobile menu.
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle?.getAttribute('aria-expanded')==='true'){toggle.click();toggle.focus()}});

})();
