//  Script that updates the text color of the <header> element
//  to red (#FF0000) when the user clicks on the tag DIV#red_header

$(function () {
  $('DIV#red_header').click(function () {
    $('HEADER').css({ color: '#FF0000' });
  });
});
