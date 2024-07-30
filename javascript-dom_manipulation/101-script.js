document.addEventListener('DOMContentLoaded', () => {
    const btnTranslate = document.getElementById('btn_translate');
    const languageCode = document.getElementById('language_code');
    const helloDiv = document.getElementById('hello');
  
    btnTranslate.addEventListener('click', () => {
      const selectedLanguage = languageCode.value;
  
      if (selectedLanguage) {
        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`)
          .then(response => response.json())
          .then(data => {
            helloDiv.textContent = data.hello;
          })
          .catch(error => {
            console.error('Error fetching the translation:', error);
            helloDiv.textContent = 'Error fetching translation';
          });
      } else {
        helloDiv.textContent = 'Please select a language';
      }
    });
  });
  