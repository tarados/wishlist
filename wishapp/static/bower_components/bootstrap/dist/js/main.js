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
    $(".select_desire").click(function () {
        var button = $(this);
        var id = button.attr("id");
        var desire_select_id = id.split("-")[1];
        var desire_select_label_id = id.split("-")[1];
        var info1 = $("#desireselect-" + desire_select_id);
        var label_select =$("#labelselect-" + desire_select_label_id);
        info1.addClass("hidden");
        label_select.removeClass("hidden");
    });
    var info = $("div.ordered");
    info.css('background', 'red');
});
