$(function () {
    // отрабатываем нажатие кнопки "edit"
    $(".edit").click(function () {
        var button = $(this);
        var id = button.attr("id");
        var desireid = id.split("-")[1];
        var info = $("#desireinfo-" + desireid);
        var form = $("#desireform-" + desireid);
        info.addClass("hidden");
        form.removeClass("hidden");
    });
    // убираем блок с кнопками у выбранного желания и отмечаем цветом
    var states = $("li.button");
    for (i=0; i<states.length; i++){
         state = states[i].getAttribute("class");
         var c = state.split("-");
         if (c[3] == 1){
             states[i].setAttribute("class", "hidden");
             // var dt = $("li.dt")[i];
             // dt.style.backgroundColor = "coral";
         }
    }
         // ссылки в желаниях открываем в другом окне
    var info2 = $("div.ordered");
    info2.css('background', 'red');
    links = $("div.well a");
    for (i=0; i<links.length; i++){
        link = links[i];
        link.target = "_blank";
    }
    // информируем об ошибке при входе
    error = $("input.error");
    box_error = $("label.box_error");
    if (error.attr("value") == 1) {
        box_error.removeClass("hidden");
    }
});
