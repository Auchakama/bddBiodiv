$('.select-all').click(function(){
    $('option', $(this).parent()).attr('selected', 'selected');
});