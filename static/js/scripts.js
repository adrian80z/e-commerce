/* flash messages disapears after 5s*/
$(document).ready(function () {
    window.setTimeout(function () {
        $(".alert").fadeTo(500, 0).slideUp(500, function () {
            $(this).remove();
        });
    }, 5000)
});