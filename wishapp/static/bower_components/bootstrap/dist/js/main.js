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
    // убираем блок с кнопками у выбранного желания и выделяем цветом
    var states = $("li.button");
    for (i=0; i<states.length; i++){
         state = states[i].getAttribute("class");
         var c = state.split("-");
         if (c[5] == "False") {
             if (c[3] == 1) {
                 states[i].setAttribute("class", "hidden");
                 var dt = $("li.dt")[i];
                 dt.style.backgroundColor = "coral";
             }
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
    // модуль перетаскивания мышкой желаний
    Sortable.create(simpleList, {onEnd: function (evt) {
        var desire_order_list = new Array();
        var desire_order = new Object();
        var desireinfo = $(".drs").each(function (index) {
            var id = $(this).attr("id");
            var desirecounter = id.split("-")[3];
            var desire_id = id.split("-")[1];
            $(".loopcounter")[index].innerHTML = index + 1;
            desire_order = {
                "desire_id": desire_id,
                "loopcounter": $(".loopcounter")[index].innerHTML
            };
            desire_order_list.push(desire_order);
        });
         list_for_save = JSON.stringify(desire_order_list);
        $.post('/order/', {"a": list_for_save});
    }});
    // кнопка "наверх"
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $(".scrollup").fadeIn();
        } else {
            $(".scrollup").fadeOut;
        }
    });
    $(".scrollup").click(function () {
        $("html, body").animate({scrollTop: 0}, 10);
        return false;
    });
});

