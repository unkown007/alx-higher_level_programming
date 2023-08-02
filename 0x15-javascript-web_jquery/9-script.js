$(document).ready(function () {
  $.getJSON(
    'https://hellosalut.stefanbohacek.dev/?lang=fr',
    (helloData) => {
      $('DIV#hello').text(helloData.name);
    }
  );
});
