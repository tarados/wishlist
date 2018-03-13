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
    $('new_desire').click(function () {
        $(window).load(function() {
            var $grid = $('.grid').masonry( masonryOptions );
            $grid.masonry('reloadItems');
        });
    });
// modal for sort*********************************************************************************************************
    var des_id = null;
    var user_id = null;
    $('a.go').click( function(event){
        event.preventDefault();
        $('#overlay').fadeIn(400,
            function(){
                $('#modal_form')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
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
            .animate({opacity: 0, top: '45%'}, 200,
                function(){
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('#modal_close, #overlay').click( function(){
    	$('#modal_form')
    		.animate({opacity: 0, top: '45%'}, 200,
    			function(){
    				$(this).css('display', 'none');
    				$('#overlay').fadeOut(400);
    			}
    		);
    });
    $('.modal_no').click(function () {
        $('#modal_form')
    		.animate({opacity: 0, top: '45%'}, 200,
    			function(){
    				$(this).css('display', 'none');
    				$('#overlay').fadeOut(400);
    			}
    		);
    });
// // modal for arc********************************************************************************************************
    var des_id = null
    var user_id = null
    $('button.del_from_arch').click( function(event){
        event.preventDefault();
        $('#overlay').fadeIn(400,
            function(){
                $('#modal_form')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
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
        $.post('/dreamers/delarchive/' + user_id + '/', desire_for_delete);
        var block = $('#doo-' + des_id + '-' + user_id);
        block.css('display', 'none');
        $('#modal_form')
            .animate({opacity: 0, top: '45%'}, 200,
                function(){
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('#modal_close, #overlay').click( function(){
    	$('#modal_form')
    		.animate({opacity: 0, top: '45%'}, 200,
    			function(){
    				$(this).css('display', 'none');
    				$('#overlay').fadeOut(400);
    			}
    		);
    });
    $('.modal_no').click(function () {
        $('#modal_form')
    		.animate({opacity: 0, top: '45%'}, 200,
    			function(){
    				$(this).css('display', 'none');
    				$('#overlay').fadeOut(400);
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


