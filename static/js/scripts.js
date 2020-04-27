/* flash messages disapears after 5s*/
$(document).ready(function () {
    window.setTimeout(function () {
        $(".alert").fadeTo(500, 0).slideUp(500, function () {
            $(this).remove();
        });
    }, 5000)


    /* animate to top scrolling */
    $("#backTop").click(function (event) {
        event.preventDefault();
        $("html, body").animate({
            scrollTop: 0
        }, "slow");
        return false;
    });
});

/* button back to top function */
$(window).scroll(function () {
    var height = $(window).scrollTop();
    if (height > 350) {
        $('#backTop').fadeIn();
    } else {
        $('#backTop').fadeOut();
    }
});