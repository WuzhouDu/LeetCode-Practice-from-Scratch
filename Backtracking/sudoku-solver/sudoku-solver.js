/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {

    let backtrack = () => {
        // console.log(board);
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {
                if (board[row][col] !== ".") continue;
                for (let num = 1; num <= 9; num++){
                    if (isValid(row, col, `${num}`, board)) {
                        board[row][col] = `${num}`;
                        if (backtrack()) {
                            return true;
                        }
                        board[row][col] = ".";
                    }
                }
                return false;
            }
        }
        return true;
    }

    let isValid = (row, col, num, board) => {
        for (let i = 0; i < 9; i++) {
            if (board[i][col] === num) return false;
        }

        for (let i = 0; i < 9; i++) {
            if (board[row][i] === num) return false;
        }

        let startRow = Math.floor(row/3) * 3;
        let startCol = Math.floor(col/3) * 3;

        for (let i = startRow; i < startRow + 3; i++) {
            for (let j = startCol; j < startCol + 3; j++) {
                if (board[i][j] === num) return false;
            }
        }

        return true;
    }

    backtrack();
};
