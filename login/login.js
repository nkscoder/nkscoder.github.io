(function () {
  const form = document.getElementById('login-form');
  const passwordInput = document.getElementById('password');
  const toggleBtn = document.getElementById('toggle-pw');

  if (toggleBtn && passwordInput) {
    toggleBtn.addEventListener('click', () => {
      const show = passwordInput.type === 'password';
      passwordInput.type = show ? 'text' : 'password';
      toggleBtn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
      toggleBtn.querySelector('.icon-show').hidden = show;
      toggleBtn.querySelector('.icon-hide').hidden = !show;
    });
  }

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = form.querySelector('#email');
      const password = form.querySelector('#password');
      let valid = true;

      [email, password].forEach((field) => {
        const wrap = field.closest('.login-field');
        if (!field.value.trim()) {
          wrap.classList.add('error');
          valid = false;
        } else {
          wrap.classList.remove('error');
        }
      });

      if (valid) {
        const btn = form.querySelector('.login-submit');
        btn.disabled = true;
        btn.querySelector('span').textContent = 'Signing in…';
        // Connect to your Django/API backend by setting form.action
        setTimeout(() => {
          btn.disabled = false;
          btn.querySelector('span').textContent = 'Sign In';
          alert('Connect this form to your backend API to enable real authentication.');
        }, 1200);
      }
    });

    form.querySelectorAll('input').forEach((input) => {
      input.addEventListener('input', () => {
        input.closest('.login-field')?.classList.remove('error');
      });
    });
  }
})();
