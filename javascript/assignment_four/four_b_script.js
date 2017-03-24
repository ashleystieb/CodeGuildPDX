/**
 * Created by ashley on 3/23/17.
 */

var diceArray = ["<img src='http://i68.tinypic.com/2w5rdsi.png'>","<img src='http://i67.tinypic.com/1039aqb.png'>",
"<img src='http://i65.tinypic.com/2pqjdc1.png'>","<img src='http://i64.tinypic.com/1111c3b.png'>",
"<img src='http://i68.tinypic.com/25koe82.png'>","<img src='http://i63.tinypic.com/2v8o5tx.png'>"];


/*
function rollDice() {
   var x = Math.floor((Math.random() * diceArray.length)); $('.dice_image').attr('src', diceArray[x]);
}
*/

$(document).ready(function(){
    $('#submit').on('click', function() {
        var num_divs = $('#number').val();
        var integer_divs = parseInt(num_divs);
        diceNumber(integer_divs);
    });
});


function diceNumber(number){
    var total = 0;
    for (var i = 0; i < number; i++){
        var x = Math.floor((Math.random() * diceArray.length)); $('.dice_image').attr('src', diceArray[x]);
        total += x+1;
        $(".input").append(diceArray[x]);
    }
    $(".total_num").append(total);
}