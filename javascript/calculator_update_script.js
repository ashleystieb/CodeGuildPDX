/**
 * Created by ashley on 3/16/17.
 */


function addNumbers(numberOne, numberTwo) {
    var one = parseInt(numberOne);
    var two = parseInt(numberTwo);
    $('.result').html(one + two);
}

function subtractNumbers(numberOne, numberTwo) {
    var one = parseInt(numberOne);
    var two = parseInt(numberTwo);
    $('.result').html(one - two);
}

function divideNumbers(numberOne, numberTwo) {
    var one = parseInt(numberOne);
    var two = parseInt(numberTwo);
    $('.result').html(one / two);
}

function multiplyNumbers(numberOne, numberTwo) {
    var one = parseInt(numberOne);
    var two = parseInt(numberTwo);
    $('.result').html(one * two);
}

$(document).ready(function () {
    $('#add').on('click', function () {
        var inputNumberOne = $('#inputOne').val();
        var inputNumberTwo = $('#inputTwo').val();
        addNumbers(inputNumberOne, inputNumberTwo);
    });
    $('#subtract').on('click', function () {
        var inputNumberOne = $('#inputOne').val();
        var inputNumberTwo = $('#inputTwo').val();
        subtractNumbers(inputNumberOne, inputNumberTwo);
    });
    $('#multiply').on('click', function () {
        var inputNumberOne = $('#inputOne').val();
        var inputNumberTwo = $('#inputTwo').val();
        multiplyNumbers(inputNumberOne, inputNumberTwo);
    });
    $('#divide').on('click', function () {
        var inputNumberOne = $('#inputOne').val();
        var inputNumberTwo = $('#inputTwo').val();
        divideNumbers(inputNumberOne, inputNumberTwo);
    })
})
