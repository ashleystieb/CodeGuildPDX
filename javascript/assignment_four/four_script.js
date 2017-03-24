/**
 * Created by ashley on 3/22/17.
 */

var diceArray = ["http://i68.tinypic.com/2w5rdsi.png","http://i67.tinypic.com/1039aqb.png",
"http://i65.tinypic.com/2pqjdc1.png","http://i64.tinypic.com/1111c3b.png",
"http://i68.tinypic.com/25koe82.png","http://i63.tinypic.com/2v8o5tx.png"];

$(document).ready(function(){
    $('#roll').on('click', function() {
        rollDice();
    });
});


function rollDice() {
   var x = Math.floor((Math.random() * diceArray.length)); $('.dice_image').attr('src', diceArray[x]);
}



/* Dice Sides 1-6
http://i68.tinypic.com/2w5rdsi.png
http://i67.tinypic.com/1039aqb.png
http://i65.tinypic.com/2pqjdc1.png
http://i64.tinypic.com/1111c3b.png
http://i68.tinypic.com/25koe82.png
http://i63.tinypic.com/2v8o5tx.png
*/