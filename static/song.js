function main() {
  $.get({
    url: 'http://127.0.0.1:5000/artist',
    success: (data) => {
      list = '';
      data.forEach((element) => {
        list +=
          `<li class="items" value=${element.id}>` + element.name + `</li>`;
      });
      tag = `<ul type="none" class="a">${list}</ul>`;
      $('div.artist').html(tag);
      console.log(data);
      console.log(tag);
    },
  });
  $(document).on('click', 'li.items', function () {
    console.log(this.value);
    $.get({
      url: `http://127.0.0.1:5000/songs/${this.value}`,
      success: (data) => {
        console.log(data);
        list = '';
        data.forEach((element) => {
          list +=
            `<li class="song" value=${element.id}>` + element.name + `</li>`;
        });
        tag = `<ul type="none" class="a">${list}</ul>`;
        $('div.songs').html(tag);
      },
    });
  });
}
$(main);
