/**
 * Created by ashley on 3/22/17.
 */

var isRight = false;

$(document).ready(function(){
    $('#button').on('click', function(){
        var marginNumber = generateNumber();
        if (isRight === false) {
            $('.square').animate({left: marginNumber});
            $('.margin_num').html(marginNumber + 'px');
            changeColor(marginNumber);
            console.log(marginNumber);
            isRight = true;
        } else {
            $('.square').animate({left: + marginNumber});
            $('.margin_num').html(marginNumber + 'px');
            changeColor(marginNumber);
            console.log(marginNumber);
            isRight = false;
        }
    })
})


function generateNumber(){
    var randomMargin = Math.floor((Math.random() * 900) + 1);
    return randomMargin;

}

function changeColor(number){
    if (number <= 250){
        $('.square').css('background-color', 'blue');
    } else if (number >= 251 && number <= 500){
        $('.square').css('background-color', 'green');
    } else if (number >= 501 && number <= 750){
        $('.square').css('background-color', 'red');
    } else if (number >= 751){
        $('.square').hide();
        $('.margin_num').html('Out of bounds');
    }
}

