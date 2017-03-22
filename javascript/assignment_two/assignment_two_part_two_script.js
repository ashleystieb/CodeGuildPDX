/**
 * Created by ashley on 3/21/17.
 */


$(document).ready(function(){
    $('#submit').on('click', function() {
        var num_divs = $('#number').val();
        var integer_divs = parseInt(num_divs);
        createSquares(integer_divs);
    });
});


function createSquares(number){
    for (var i = 0; i < number; i++){
        $(".container").append('<div class="square"></div>');
    }
}