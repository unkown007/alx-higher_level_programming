$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: (data, textStatus, xhr) => {
      $('DIV#hello').text(`${data.hello}`);
    }
  });
});
