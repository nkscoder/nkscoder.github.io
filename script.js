(function () {
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      const open = navLinks.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open);
    });

    navLinks.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  const params = new URLSearchParams(window.location.search);
  if (params.get('sent') === 'true') {
    const form = document.querySelector('.contact-form');
    const success = document.getElementById('form-success');
    if (form && success) {
      form.hidden = true;
      success.hidden = false;
    }
  }
})();
