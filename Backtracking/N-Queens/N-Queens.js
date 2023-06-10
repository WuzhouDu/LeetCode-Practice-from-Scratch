/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    let res = [];
    let path = [];
    let globalTable = [];
    for (let i = 0; i < n; i++){
        globalTable[i] = [];
        for (let j = 0; j < n; j++) {
            globalTable[i][j] = 0;
        }
    }
    
    let updateTable = function(start, down, index) {
        
        for (let i = start+1; i < n; i++) {
            let offset = i - start;
            // console.log("offset:", offset);
            globalTable[i][index] -= (down ? 1 : -1);
            if (index-offset >= 0) {
                globalTable[i][index-offset] -= (down ? 1 : -1);
            }
            if (index+offset < n) {
                globalTable[i][index+offset] -= (down ? 1 : -1);
            }
            // console.log(globalTable[i])
        }
    }

    let backtrack = (start) => {
        if (path.length === n) {
            res.push([...path]);
            return;
        }
        // console.log(path);
        // console.log(globalTable);
        for (let i = 0; i < n; i++) {
            if (globalTable[start][i] >= 0){
                path.push(".".repeat(i)+"Q"+".".repeat(n-i-1));
                updateTable(start, true, i);
                backtrack(start+1);
                updateTable(start, false, i);
                path.pop();
            }
        }
    }

    backtrack(0);
    return res;
};