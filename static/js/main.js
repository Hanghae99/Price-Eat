$(document).ready(function () {
  show_store();
});

function show_store() {
  $.ajax({
    type: "GET",
    url: "/store",
    data: {},
    success: function (response) {
      console.log(response);
      let rows = response["stores_list"];
      for (let i = 0; i < rows.length; i++) {
        let name = rows[i]["name"];
        let address = rows[i]["adress"];
        let store_img = rows[i]["store_img"];
        let temp_html = `<div class="desc_list" onclick="location.href='/store_desc?name=${name}'">
                          <div class="store_img" style="background-image: url(${store_img});">
                          </div>
                          <div class="store_name">
                            ${name}
                          </div>
                        </div>`;
        $("#list_box").append(temp_html);
      }
    },
  });
}
