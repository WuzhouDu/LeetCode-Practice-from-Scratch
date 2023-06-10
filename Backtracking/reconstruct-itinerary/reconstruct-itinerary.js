/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    let path = ["JFK"];
    let res = [];
    let globalUsed = [];

    let backtrack = () => {
        if (path.length === tickets.length + 1) {
            res.push(path.slice());
            return;
        }

        for (let i = 0; i < tickets.length; i++) {
            if (globalUsed[i]) continue;
            // console.log(path);
            if (tickets[i][0] === path[path.length-1] && localUsed.indexOf(tickets[i][1]) === -1) {
                globalUsed[i] = true;
                localUsed.push(tickets[i][1]);
                path.push(tickets[i][1]);
                // console.log("find.");
                backtrack();
                // console.log("pop");
                path.pop();
                globalUsed[i] = false;
            }
            else {
                continue;
            }
        }
    }

    backtrack();
    res.sort();
    return res[0];
};