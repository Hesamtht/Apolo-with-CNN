// Script for displaying images on menu item click
$(document).ready(function() {
    $('.menu-item').click(function() {
        var imageUrl = $(this).data('image');
        $('#item-image').attr('src', imageUrl);
        $('#item-modal').modal('show');
    });
});
