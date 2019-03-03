function entry(e, item) {
    let charval = String.fromCharCode(e.keyCode);
    if (((isNaN(charval)) && (e.which !== 8) && (e.which !== 9)) ||
        (item.value.length > 0 && (e.which !== 8) && (e.which !== 9))) { // BSP KB code is 8
        return false;
    }

    return true;
}

// function moveCell(e, item) {
//     return false;
//     let charval = String.fromCharCode(e.keyCode);
//     if (entry(e, item)) {
//         return false
//     }
//     var currentCell = item.parentElement.getAttribute("id");
//     var num = Number(currentCell.slice(-1));
//     num += 1;
//     currentCell = currentCell.slice(0, currentCell.length - 1);
//     currentCell = currentCell + num.toString();
//     document.getElementById(currentCell).firstChild.focus();
// }

function clearBoard() {
    let board = document.getElementsByClassName("cell_input");
    for (var i = 0; i < board.length; i++) {
        board[i].value = "";
    }
    document.getElementById("sudoku_iters").innerText = '--';

}

// function populateBoard() {
//     let board = document.getElementsByClassName("cell_input");
//     let solution = "{{ sudoku.sudoku }}";
//     for (var i = 0; i < board.length; i++) {
//         board[i].value = solution.charAt(i);
//     }
//
// }

function ajaxPopulateBoard(solution) {
    let board = document.getElementsByClassName("cell_input");
    for (var i = 0; i < board.length; i++) {
        board[i].value = solution.charAt(i);
    }

}

function parseBoard() {
    let board = document.getElementsByClassName("cell_input");
    var nums = "";
    for (var i = 0; i < board.length; i++) {
        if (board[i].value.toString() === "") {
            nums += "-";
        } else {
            nums += board[i].value.toString();
        }
    }
    document.getElementById('nums').value = nums;
    return nums;
}

function setVal() {
    let board = document.getElementsByClassName("cell_input");
    for (var i = 0; i < board.length; i++) {
        board[i].value = 3;
    }
}


