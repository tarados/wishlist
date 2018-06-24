$(function () {
    $(window).load(function() {
        var $grid = $('.grid').masonry( masonryOptions );
        $grid.masonry('reloadItems');
    });
});