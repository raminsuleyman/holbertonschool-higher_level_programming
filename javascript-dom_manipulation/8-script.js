document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloDiv = document.querySelector('#hello');

  fetch(url)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      helloDiv.textContent = data.hello;
    });
});
