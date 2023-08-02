$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data, textStatus) => {
  const films = data.results;
  films.forEach((film) => {
    $('UL#list_movies').append($('<li></li>').text(`${film.title}`));
  });
});
