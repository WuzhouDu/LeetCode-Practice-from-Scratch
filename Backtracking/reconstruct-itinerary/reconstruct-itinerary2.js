/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    let path = ["JFK"];
    let res = [];
    let globalUsed = [];

    let backtrack = () => {
        if (res.length === 1) return;
        if (path.length === tickets.length + 1) {
            res.push(path.slice());
            return;
        }

        let validElements = [];
        for (let i = 0; i < tickets.length; i++) {
            if (globalUsed[i]) continue;
            if (tickets[i][0] === path[path.length-1]) {
                validElements.push([tickets[i][1], i]);
            }
        }
        validElements.sort((a, b) => {
            if (a[0] < b[0]) return -1;
            else if (a[0] == b[0]) return 0;
            else return 1;
        });


        for (let i = 0; i < validElements.length; i++) {
            if (i > 0 && validElements[i-1][0] === validElements[i][0]) {
                continue;
            }
            globalUsed[validElements[i][1]] = true;
            path.push(validElements[i][0]);
            backtrack();
            path.pop();
            globalUsed[validElements[i][1]] = false;
        }

    }

    backtrack();
    return res[0];
};