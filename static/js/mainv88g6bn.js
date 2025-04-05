document.addEventListener('DOMContentLoaded', () => {
  // Filename
  document.querySelectorAll('input[type=file]').forEach(input => {
    input.addEventListener('change', function (e) {
      const closestField = this.closest('.order-b__file');

      if (closestField) {
        const noteElement = closestField.querySelector('span');

        if (noteElement) {
          const fileName = this.value.replace(/^.*[\\\/]/, '');
          noteElement.textContent = fileName;
        }
      }
    });
  }); // Mask Input

  const phoneInputs = document.querySelectorAll('.input-text_phone');
  if (phoneInputs.length === 0) return;

  function maskPhone(event) {
    let matrix = '+7 (___) ___-__-__',
        i = 0,
        def = matrix.replace(/\D/g, ''),
        val = event.target.value.replace(/\D/g, '');
    if (def.length >= val.length) val = def;
    event.target.value = matrix.replace(/./g, function (a) {
      return /[_\d]/.test(a) && i < val.length ? val.charAt(i++) : i >= val.length ? '' : a;
    });

    if (event.type === 'blur' && event.target.value.length < matrix.length) {
      event.target.value = '';
    }
  }

  function onPhoneFocus(event) {
    if (!event.target.value) {
      event.target.value = '+7 (';
      event.target.selectionStart = event.target.value.length;
    }
  }

  phoneInputs.forEach(input => {
    input.addEventListener('input', maskPhone);
    input.addEventListener('focus', onPhoneFocus);
    input.addEventListener('blur', maskPhone);
  });
});