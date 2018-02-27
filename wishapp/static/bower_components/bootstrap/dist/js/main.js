$(function () {
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
 // отрабатываем нажатие кнопки "обновить"*******************************************************************
    $("button.view").click(function () {
        var button = $(this);
        var id = button.attr("id");
        var desireid = id.split("-")[1];
        var info = $(".list-group-item");
        var form = $("div.grid");
        var block = $("#add_desire_block");
        var text = id.split("-")[5];
        var title = id.split("-")[7];
        $('#desire_title').attr('value', title);
        $('.desire_id').attr('value', desireid);
        $('#id_desire_text_for_edit').text(text);
        info.removeClass("hidden");
        block.css('display', 'none');
        form.css('display', 'none');
        console.log(desireid);
        console.log(title);
        console.log(text);
        console.log($('.desire_id'));
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
            button_guest.css('background-color', '#e74c3c');
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
    $('.new_desire').click(function () {
            var block = $("#add_desire_block");
            var form = $("div.grid");
            block.removeClass('hidden');
            form.css('display', 'none');
        });
// modal*********************************************************************************************************
    var des_id = null
    var user_id = null
    $('a.go').click( function(event){ // лoвим клик пo ссылки с id="go"
        event.preventDefault(); // выключaем стaндaртную рoль элементa
        $('#overlay').fadeIn(400, // снaчaлa плaвнo пoкaзывaем темную пoдлoжку
            function(){ // пoсле выпoлнения предъидущей aнимaции
                $('#modal_form')
                    .css('display', 'block') // убирaем у мoдaльнoгo oкнa display: none;
                    .animate({opacity: 1, top: '50%'}, 200);// плaвнo прибaвляем прoзрaчнoсть oднoвременнo сo съезжaнием вниз
        });
        des_id = this.id.split('-')[1];
        user_id = this.id.split('-')[2];
    });
    $('.modal_yes').click(function () {
        var desire_for_delete = new Object();
        desire_for_delete = {
            "deldesire": des_id
        };
        obj_for_save = JSON.stringify(desire_for_delete);
        $.post('/dreamers/del_sort_desire/' + user_id + '/', desire_for_delete);
        var block = $('#do-' + des_id + '-' + user_id);
        block.css('display', 'none');
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,  // плaвнo меняем прoзрaчнoсть нa 0 и oднoвременнo двигaем oкнo вверх
                function(){ // пoсле aнимaции
                    $(this).css('display', 'none'); // делaем ему display: none;
                    $('#overlay').fadeOut(400); // скрывaем пoдлoжку
                }
            );
    });
    	/* Зaкрытие мoдaльнoгo oкнa, тут делaем тo же сaмoе нo в oбрaтнoм пoрядке */
    $('#modal_close, #overlay').click( function(){ // лoвим клик пo крестику или пoдлoжке
    	$('#modal_form')
    		.animate({opacity: 0, top: '45%'}, 200,  // плaвнo меняем прoзрaчнoсть нa 0 и oднoвременнo двигaем oкнo вверх
    			function(){ // пoсле aнимaцииo
    				$(this).css('display', 'none'); // делaем ему display: none;
    				$('#overlay').fadeOut(400); // скрывaем пoдлoжку
    			}
    		);
    });
    $('.modal_no').click(function () {
        $('#modal_form')
    		.animate({opacity: 0, top: '45%'}, 200,  // плaвнo меняем прoзрaчнoсть нa 0 и oднoвременнo двигaем oкнo вверх
    			function(){ // пoсле aнимaции
    				$(this).css('display', 'none'); // делaем ему display: none;
    				$('#overlay').fadeOut(400); // скрывaем пoдлoжку
    			}
    		);
    });

//**************************************************************************************************************;
    Sortable.create(simpleList, {
        onEnd: function () {
            var desire_order_list = new Array();
            var desire_order = new Object();
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
            console.log(list_for_save);
        },
        ghostClass: "ghost"
    });
});


