const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = document.querySelector('#list_movies');

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      const newLi = document.createElement('li');
      newLi.textContent = movie.title;
      listMovies.appendChild(newLi);
    });
  });
