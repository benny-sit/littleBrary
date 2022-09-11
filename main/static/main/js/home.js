// $(window).scroll(() => {
//     scaleContent();
// })

// function scaleContent() {
//     var wScroll = $(window).scrollTop();

//     if ($('#home-content').length) {
//         $('#home-content').css('transform', 'scale(1.05)');
//     }
// }
// console.log("HII");

$(() => {
    $('#home-wrapper').scroll( () => {
        let scrolled = $('#home-wrapper').scrollTop()
        $('#home-title').css('opacity', 1 - scrolled/900);
        if (scrolled < 400 && $(window).width() > 992) {
            $('#home-content').css('transform', `translateZ(-5px) scale(${1.15 + scrolled/2500}) translateY(-${scrolled/3}px)`);
        } else if ($(window).width() < 992 && scrolled > 0) {
            $('#home-content').css('transform', 'translateZ(-5px) scale(1.2) translateY(32%)');
        } else if ($(window).width() < 992 && scrolled == 0) {
            $('#home-content').css('transform', 'translateZ(-5px) scale(1.2) translateY(38%)');
        } 

        if ($(window).width() > 992) {
            if (scrolled > 550) {
                $('#home-main-text').css('opacity', 1 - (scrolled - 550) / 800);
                $('#home-float-left').css('transform', `translateZ(-1px) scale(1.2) translateX(0)`);
                $('#home-float-right').css('transform', `translateY(40%) translateZ(-2px) scale(1.2) translateX(0)`);
            } else {
                $('#home-float-left').css('transform', `translateZ(-1px) scale(1.1) translateX(-100%)`);
                $('#home-float-right').css('transform', `translateY(40%) translateZ(-2px) scale(1.1) translateX(100%)`);
            }    
        }
    });

});


