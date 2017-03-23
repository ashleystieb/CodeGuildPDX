/**
 * Created by ashley on 3/22/17.
 */

var isRight = false;

$(document).ready(function(){
    $('.square').on('click',function(){
        if (isRight === false) {
            $('.square').css('margin-left','300px');
            isRight = true;
        } else {
            $('.square').css('margin-left','0');
            isRight = false;
        }
    })
})

/*
$(".rectangle").on('click', function(){
    $(".rectangle").animate({left: '300px'});
});
*/

var isRightRec = false;

$(document).ready(function(){
    $('.rectangle').on('click', function(){
        if (isRightRec === false) {
            $('.rectangle').animate({left: '300px'});
            isRightRec = true;
        } else {
            $('.rectangle').animate({left: '0'});
            isRightRec = false;
        }
    })
})