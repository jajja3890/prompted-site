(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.getElementById('mobile-menu');
  if (toggle && nav) {
    const close = () => { toggle.setAttribute('aria-expanded','false'); nav.hidden = true; };
    toggle.addEventListener('click', () => {
      const opened = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!opened)); nav.hidden = opened;
    });
    nav.querySelectorAll('a').forEach(a=>a.addEventListener('click', close));
    window.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }
})();
