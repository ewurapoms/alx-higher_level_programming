// Script that fetches and lists the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies

$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
