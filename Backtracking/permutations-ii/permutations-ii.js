/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    let usedGlobal = [];
    let path = [];
    let res = [];

    let backtrack = () => {
        if (path.length === nums.length) res.push([...path]);

        let usedLocal = {};
        for (let i = 0; i < nums.length; i++) {
            if (usedGlobal[i] || usedLocal.hasOwnProperty(`${nums[i]}`)) {
                continue;
            }
            else {
                path.push(nums[i]);
                usedGlobal[i] = true;
                usedLocal[nums[i]] = true;
                backtrack();
                path.pop();
                usedGlobal[i] = false;
            }
        }
    }

    backtrack();
    return res;
};