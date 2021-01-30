/**
 * This updates and removes product quantity using 
 * '+' and '-' buttons and
 * reloads the page
 */
$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();

})

$('.delete-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = '/cart/delete/$(itemId)';
    var data = {'csrfmiddlewartoken': csrfToken};

    $.post(url, data)
        .done(function() {
            location.reload();
        });
})


