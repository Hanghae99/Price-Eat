
function getInputValue() {
  $('#list_box').empty()
  let area = $('#area').val()
  let price = $('#price').val()

  $.ajax({
    type: 'POST',
    url: '/search',
    data: {guname_give: area, price_give: price},
    success: function (response) {
      let rows = response["final_list"];
      for (let key in rows) {
        let name = key
        let url = rows[key]
        console.log(key)
        let temp_html = `<div class="desc_list" onclick="location.href='/store_desc?name=${name}'">
                            <div class="store_img" style="background-image: url('${url}');">
                            </div>
                            <div class="store_name">
                            ${name}
                            </div>
                          </div>`;
        $("#list_box").append(temp_html);
      }
    }
  });
}