$(function () {
    $(".edit").click(function () {
        var button = $(this);
        var id = button.attr("id");
        var desireid = id.split("-")[1];
        var info = $("#desireinfo-" + desireid);
        var form = $("#desireform-" + desireid);
        info.addClass("hidden");
        form.removeClass("hidden");
    });

    console.log($("div.st").length);


    var info2 = $("div.ordered");
    info2.css('background', 'red');
    links = $("div.well a");
    for (i=0; i<links.length; i++){
        link = links[i];
        link.target = "_blank";
    }
    error = $("input.error");
    box_error = $("label.box_error");
    if (error.attr("value") == 1) {
        box_error.removeClass("hidden");
    }
});
