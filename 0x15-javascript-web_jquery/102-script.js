$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${code}`,
      type: 'GET',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
