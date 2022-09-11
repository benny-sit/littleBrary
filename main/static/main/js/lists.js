
$( () => {
    console.log('Loading...');
    $('#btn-new-list').click( () => {
        $('#add-list').removeClass('unseen');
    });
    $('#btn-remove-list').click( () => {
        $('#add-list').addClass('unseen');
        $('#list_name').val('');
    });
});