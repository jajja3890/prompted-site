(()=>{
'use strict';
const toggle=document.querySelector('.nav-toggle');
const nav=document.querySelector('.mobile-nav');
if(!toggle||!nav)return;
const openLabel=document.documentElement.lang==='en'?'Open menu':'Avaa valikko';
const closeLabel=document.documentElement.lang==='en'?'Close menu':'Sulje valikko';
function setMenu(open){
 toggle.setAttribute('aria-expanded',String(open));
 toggle.setAttribute('aria-label',open?closeLabel:openLabel);
 nav.setAttribute('aria-hidden',String(!open));
}
toggle.addEventListener('click',()=>setMenu(toggle.getAttribute('aria-expanded')!=='true'));
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
document.addEventListener('keydown',e=>{
 if(e.key==='Escape'&&toggle.getAttribute('aria-expanded')==='true'){
  setMenu(false);toggle.focus();
 }
});
document.addEventListener('click',e=>{
 if(toggle.getAttribute('aria-expanded')==='true'&&!toggle.contains(e.target)&&!nav.contains(e.target))setMenu(false);
});
window.addEventListener('resize',()=>{
 if(window.innerWidth>1040&&toggle.getAttribute('aria-expanded')==='true')setMenu(false);
});
})();
