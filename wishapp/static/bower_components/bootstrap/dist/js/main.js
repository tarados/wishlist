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
});
$(function () {
    $(".select_desire").click(function () {
        var button = $(this);
        var id = button.attr("id");
        var desire_select_id = id.split("-")[1];
        var desire_select_label_id = id.split("-")[1];
        var info = $("#desireselect-" + desire_select_id);
        var label_select =$("#labelselect-" + desire_select_label_id);
        info.addClass("hidden");
        label_select.removeClass("hidden");
        console.log('jfksdgja');
    });
});

$(function () {
    alert('dfhfj');
    // var info = $("div.well");
    console.log("info");
});
