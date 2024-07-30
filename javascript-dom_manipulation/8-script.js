const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

const fetchHello = () => {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const helloElement = document.getElementById('hello');
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching the hello translation:', error);
    });
};

document.addEventListener('DOMContentLoaded', fetchHello);