/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let start = 0;
    let res = 0;
    while (start < nums.length - 1) {
        if (start + nums[start] >= nums.length - 1) return res + 1;
        let max = 0;
        let maxIndex = 0;
        for (let i = 1; i <= nums[start]; i++) {
            if (max < start + i + nums[start+i]) {
                max = start + i + nums[start+i];
                maxIndex = start + i;
            }
        }
        start = maxIndex;
        res++;
    }
    return res;
};