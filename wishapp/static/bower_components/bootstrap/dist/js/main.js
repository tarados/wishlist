$(function () {
    $(".edit").click(function () {
        var button = $(this);
        var id = button.attr("id");
        var desireid = id.split("-")[1];
        var info = $("#desireinfo-" + desireid);
        var form = $("#desireform-" + desireid);
        // var strold = form.text().substring(form.text().indexOf("<a href"), form.text().indexOf("</a>") + 4);
        // var strnew = form.text().substring(form.text().indexOf(">http") +1, form.text().indexOf("</a>"));
        // var newform = form.text().replace(strold, strnew);
        var textarea = $("textarea", form);
        var str = textarea.text();
        info.addClass("hidden");
        form.removeClass("hidden");
        console.log(str.indexOf(">http", 72));
    });
});
