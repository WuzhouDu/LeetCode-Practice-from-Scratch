/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    if (nums.length === 1) return nums[0];

    var res = -Math.pow(10, 4);
    var count = res;

    for (let i = 0; i < nums.length; i++) {
        if (count < 0) {
            count = nums[i];
        }
        else if (count+nums[i] < 0) {
            count = nums[i];
        }
        else {
            count += nums[i];
        }

        if (count > res) {
            res = count;
        }
    }

    return res;
};