$(function () {
    // отрабатываем нажатие кнопки "edit"
    $(".edit").click(function () {
        var button = $(this);
        var id = button.attr("id");
        var desireid = id.split("-")[1];
        // var info = $("#desireinfo-" + desireid);
        var form = $("#desireform-" + desireid);
        // info.addClass("hidden");
        form.removeClass("hidden");
    });
    // ссылки в желаниях открываем в другом окне
    var info2 = $("div.ordered");
    info2.css('background', 'red');
    links = $("li.tx a");
    for (i = 0; i < links.length; i++) {
        link = links[i];
        link.target = "_blank";
    }
    // информируем об ошибке при входе
    error = $("input.error");
    box_error = $("label.box_error");
    if (error.attr("value") == 1) {
        box_error.removeClass("hidden");
    }
    // кнопка "наверх"
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $(".scrollup").fadeIn();
        } else {
            $(".scrollup").fadeOut();
        }
    });
    $(".scrollup").click(function () {
        $("html, body").animate({scrollTop: 0}, 10);
        return false;
    });
// анимация******************************************************************************************************
    function init() {
        var speed = 250,
            easing = mina.easeinout;

        [].slice.call ( document.querySelectorAll( '#grid > #simpleList > div.grid-link' ) ).forEach( function( el ) {
            var s = Snap( el.querySelector( 'svg' ) ), path = s.select( 'path' ),
                pathConfig = {
                    from : path.attr( 'd' ),
                    to : el.getAttribute( 'data-path-hover' )
                };

            el.addEventListener( 'mouseenter', function() {
                path.animate( { 'path' : pathConfig.to }, speed, easing );
            } );

            el.addEventListener( 'mouseleave', function() {
                path.animate( { 'path' : pathConfig.from }, speed, easing );
            } );
        } );
    }

    init();
 // отрабатываем нажатие кнопки "view"*******************************************************************
    $("button.view").click(function () {
        var button = $(this);
        var id = button.attr("id");
        var desireid = id.split("-")[1];
        var info = $("#row-" + desireid);
        var form = $("#grid div.grid-link");
        var block = $("#add_desire_block");
        info.removeClass("hidden");
        block.addClass("hidden");
        form.addClass("hidden");
    });
    $("div.visitor").each(function () {
        var state = (this.id).split('-')[9];
        var loggedin = (this.id).split('-')[3];
        var choice = (this.id).split('-')[5];
        var desire = (this.id).split('-')[7];
        var button_guest = $("#desireselect-" + desire);
        var button_noname = $("#noname-" + desire);
        var button_view = $("#view-" + desire);
        var button_arch = $("#ar-" + desire);
        if (state == 1) {
            button_guest.text('выбрано');
            button_noname.text('выбрано');
            button_guest.css('background-color', 'red');
            button_noname.css('background-color', 'red');
        }
        if (loggedin == 'True') {
            button_view.addClass('hidden');
            button_arch.addClass('hidden');
            button_noname.removeClass('hidden');
        } else if (choice == 'True') {
            button_view.addClass('hidden');
            button_arch.addClass('hidden');
            button_guest.removeClass('hidden');
        }
    });
    Sortable.create(simpleList, {
        onEnd: function () {
            var desire_order_list = new Array();
            var desire_order = new Object();
            $("figcaption > h2").each(function (index) {
                var loopcounter = this.id.split('-')[1];
                var desire_id = this.id.split('-')[3];
                desire_order = {
                    "desire_id": desire_id,
                    "loopcounter": index + 1
                };
                desire_order_list.push(desire_order);
            });
            list_for_save = JSON.stringify(desire_order_list);
            $.post('/order/', {"a": list_for_save});
        }
    });
    $('.al:even').css("margin", "30px");
});

