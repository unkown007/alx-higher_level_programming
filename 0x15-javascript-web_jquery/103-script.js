const setHello = () => {
  const code = $('INPUT#language_code').val();
  $.ajax({
    url: `https://hellosalut.stefanbohacek.dev/?lang=${code}`,
    type: 'GET',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
};
$(document).ready(() => {
  $('INPUT#btn_translate').click(setHello);
  $('INPUT#language_code').on('keypress', (event) => {
    if (event.which === 13) {
      setHello();
    }
  });
});
