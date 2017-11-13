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
    // var states = $("li.button").attr("class", "hidden");
    // states.addClass("hidden");
    // for (i=0; i<states.length; i++){
    //      state = states[i].getAttribute("class");
    //      // states.addClass("hidden");
    //      var c = state.split("-");
    //      if (c[3] == 1) {
    //          var b = states[i];
    //          // b.addClass("hidden");
    //      }
    //      console.log(typeof b);
    // }
    var d = html('<li class="list-group-item button desirestate-{{ desire.desire_state }}"></li>');
    console.log(d);
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
