const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const characterDiv = document.querySelector('#character');

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    characterDiv.textContent = data.name;
  });
