$('DIV#toggle_header').click(() => {
  const header = $('header');
  if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  } else {
    header.removeClass('red');
    header.addClass('green');
  }
});
