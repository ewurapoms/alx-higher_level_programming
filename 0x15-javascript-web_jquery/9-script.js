// Script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello
// The translation of “hello” must be displayed in the HTML tag DIV#hello

$.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      method: 'GET',
      dataType: 'json',
      success: function (data) {
        const translation = data.hello;
        $('DIV#hello').text(translation);
      }
});
