// Script that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/people/5/?format=json',
    success: function (data) {
      $('DIV#character').text(data.name);
    }
  });
});
