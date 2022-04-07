function main() {
  $.get({
    url: 'http://127.0.0.1:5000/artist',
    success: (data) => {
      list = '';
      data.forEach((element) => {
        list += '<li class="items">' + element.name + '</li>';
      });
      tag = `<ul type="none" class="a">${list}</ul>`;
      $('div.artist').html(tag);
      console.log(data);
      console.log(tag);
    },
  });
  $(document).on('click', 'li.items', function () {
    alert($(this).text());
  });
}
$(main);
