/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    if (nums.length === 1) return 1;
    let res = 1;
    let prev = 0;
    let cur = 0;

    for (let i = 0; i < nums.length-1; i++) {
        cur = nums[i+1] - nums[i];
        if ((prev <= 0 && cur > 0) || (prev >= 0 && cur < 0)) {
            res++;
            prev = cur;
        }
    }
    return res;

};