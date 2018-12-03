$(function () {
    $('a.new_desirelist').click(function (event) {
        event.preventDefault();
        $('#overlay1').fadeIn(400,
            function () {
                $('#modal_form1')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
            });
    });
    /* Зaкрытие мoдaльнoгo oкнa, тут делaем тo же сaмoе нo в oбрaтнoм пoрядке */
    $('#modal_close1, #overlay1, .add_desirelist_form_button').click(function () {
        $('#modal_form1')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay1').fadeOut(400);
                }
            );
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
        var $cache = $('.fixed');
        if ($(this).scrollTop() > 100) {
            $cache.css({
                'position': 'fixed',
                'top': '0px',
                'opacity': '1'
            });
            $(".scrollup").fadeIn();
        } else {
            $cache.css({
                'position': 'relative',
            });
            $(".scrollup").fadeOut();
        }
    });
    $(".scrollup").click(function () {
        $("html, body").animate({scrollTop: 0}, 10);
        return false;
    });
    $(".desire_button").each(function () {
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
            button_noname.each(function () {
                this.disabled = true;
            });
            button_guest.css('opacity', '0');
            button_noname.css('background-color', '#e74c3c');
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

// modal for sort*********************************************************************************************************
    var des_id = null;
    var sub_id = null;
    $('a.go').click(function (event) {
        event.preventDefault();
        $('#overlay').fadeIn(400,
            function () {
                var scrol = $(window).scrollTop() + 270;
                $('#modal_form')
                    .css('display', 'block')
                    .animate({opacity: 1, top: scrol}, 200);
            });
        des_id = this.id.split('-')[1];
        sub_id = this.id.split('-')[2];
    });
    $('.modal_yes').click(function () {
        var desire_for_delete_sort = new Object();
        desire_for_delete_sort = {
            "deldesire_sort": des_id
        };
        var sort_block = $('a.go');
        if (sort_block.length > 0) {
            $.post('/dreamers/del_sort_desire/' + sub_id + '/', desire_for_delete_sort);
        }
        var block = $('#do-' + des_id + '-' + sub_id);
        block.css('display', 'none');
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('#modal_close, #overlay').click(function () {
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('.modal_no').click(function () {
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
// modal for arc********************************************************************************************************
    var des_id = null
    var sub_id = null
    $('button.del_from_arch').click(function (event) {
        event.preventDefault();
        $('#overlay').fadeIn(400,
            function () {
                $('#modal_form')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
            });
        des_id = this.id.split('-')[1];
        sub_id = this.id.split('-')[2];
    });
    $('.modal_yes').click(function () {
        var desire_for_delete_archiv = new Object();
        desire_for_delete_archiv = {
            "deldesire_arch": des_id
        };
        var arch_block = $("button.del_from_arch");
        if (arch_block.length > 0) {
            $.post('/dreamers/delarchive/' + sub_id + '/', desire_for_delete_archiv);
        }
        var block = $('#doo-' + des_id + '-' + sub_id);
        block.css('display', 'none');
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('#modal_close, #overlay').click(function () {
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('.modal_no').click(function () {
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
// modal for desirelist delete*********************************************************************************************************
    var deslist_id = null;
    var user_id = null;
    $('a.go1').click(function (event) {
        event.preventDefault();
        $('#overlay').fadeIn(400,
            function () {
                $('#modal_form')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
            });
        deslist_id = this.id.split('-')[1];
        user_id = this.id.split('-')[2];
    });
    $('.modal_yes').click(function () {
        var desirelist_for_delete = new Object();
        desirelist_for_delete = {
            "deldesirelist": deslist_id
        };
        var list_block = $('a.go1');
        if (list_block.length > 0) {
            $.post('/dreamers/deldesirelist/' + user_id + '/', desirelist_for_delete);
        }
        var block = $('#do-' + deslist_id + '-' + user_id);
        block.css('display', 'none');
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('#modal_close, #overlay').click(function () {
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('.modal_no').click(function () {
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
// return from archive****************************************************************************************
    $('.return_from_arch').click(function () {
        var desireforreturn = new Object();
        var user_id = (this.id).split('-')[2];
        var desire_id = (this.id).split('-')[1];
        desireforreturn = {
            'returndesire': desire_id
        };
        $.post('/dreamers/returnfromarchive/' + user_id + '/', desireforreturn);
        var block = $('#doo-' + desire_id + '-' + user_id);
        block.css('display', 'none');
    });

//**************************************************************************************************************;
    if ($('#simpleList')[0] != undefined) {
        var sor = $('#simpleList')[0];
        Sortable.create(simpleList, {
            onEnd: function () {
                var desire_order_list = new Array();
                var desire_order = new Object();
                var sortcounter = new Array();
                $('.sortcounter').each(function (index) {
                    $(this).html(index + 1);
                });
                $(".desire_title").each(function (index) {
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
            },
            ghostClass: "ghost"
        });
    }
    ;
    $('a.copy_to_clipboard').click(function () {
        var part_link = $(this).attr('id');
        var domen_name = document.location.origin;
        var link_send = domen_name + part_link;
        var textArea = document.createElement("textarea");
        textArea.value = link_send;
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        document.execCommand('copy');
        $('textArea').addClass('hidden');
    })
// masonry*************************************************************************************
    var $grid = $('.grid').masonry({
        // disable initial layout
        initLayout: false,
        //...
    });
// bind event
    $grid.masonry('on', 'layoutComplete', function () {
        console.log('layout is complete');
    });
// trigger initial layout
    $grid.masonry();

// modal for desire*********************************************************************************************************
    $('a.new_desire').click(function (event) {
        event.preventDefault();
        $('#overlay2').fadeIn(400,
            function () {
                var scrol = $(window).scrollTop() + 270;
                $('#modal_form2')
                    .css('display', 'block')
                    .animate({opacity: 1, top: scrol}, 200);
            });
    });
    /* Зaкрытие мoдaльнoгo oкнa, тут делaем тo же сaмoе нo в oбрaтнoм пoрядке */
    $('#modal_close2, #overlay2, .add_desire_form_button').click(function () {
        $('#modal_form2')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay2').fadeOut(400);
                }
            );
    });
    // modal for desire edit*********************************************************************************************************
    $('button.edit_desire').click(function (event) {
        event.preventDefault();
        $('#overlay3').fadeIn(400,
            function () {
                var scrol = $(window).scrollTop() + 270;
                $('#modal_form3')
                    .css('display', 'block')
                    .animate({opacity: 1, top: scrol}, 200);
            });
        var button = $(this);
        var id = button.attr("id");
        var desireid = id.split("§")[1];
        var text = id.split("§")[5];
        var title = id.split("§")[7];
        $('#desire_title').attr('value', title);
        $('.desire_id').attr('value', desireid);
        $('#id_desire_text_for_edit').text(text);
    });
    /* Зaкрытие мoдaльнoгo oкнa, тут делaем тo же сaмoе нo в oбрaтнoм пoрядке */
    $('#modal_close3, #overlay3, .edit_desire_from_button').click(function () {
        $('#modal_form3')
            .animate({opacity: 0, top: '45%'}, 200,
                function () {
                    $(this).css('display', 'none');
                    $('#overlay3').fadeOut(400);
                }
            );
    });

});