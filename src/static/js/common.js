$(function(){
});

// スクロールでフェードイン
$(window).scroll(function () {
    $('.fadein').each(function () {
        var elemPos = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > elemPos - windowHeight) {
            $(this).addClass('scrollin');
        }
    });
});

// アクセス時フェードイン
$(window).ready(function () {
    $('.fadein-right').each(function () {
        var elemPos = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > elemPos - windowHeight) {
            $(this).addClass('scrollin');
        }
    });
});

$(window).ready(function () {
    $('.fadein-left').each(function () {
        var elemPos = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > elemPos - windowHeight) {
            $(this).addClass('scrollin');
        }
    });
});

$(window).ready(function () {
    $('.fadein-center').each(function () {
        var elemPos = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > elemPos - windowHeight) {
            $(this).addClass('scrollin');
        }
    });
});