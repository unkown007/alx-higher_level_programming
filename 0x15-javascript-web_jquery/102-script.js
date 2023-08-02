$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();
    /* $.getJSON(
      `https://stefanbohacek.com/hellosalut/?lang=${code}`,
      (data) => {
        $('DIV#hello').text(data.hello);
      }
    ); */
    $.support.cors = true;
    $.ajax({
      url: `https://stefanbohacek.com/hellosalut/?lang=${code}`,
      type: 'GET',
      dataType: 'jsonp',
      contentType: 'application/json',
      success: function (data) {
        // alert(data);
      },
      error: function (jqXHR, textStatus, ex) {
        // alert(textStatus + "," + ex + "," + jqXHR.responseText);
      }
    });
  });
});
