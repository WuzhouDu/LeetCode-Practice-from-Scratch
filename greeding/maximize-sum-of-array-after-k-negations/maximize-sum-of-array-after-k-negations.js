/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var largestSumAfterKNegations = function(nums, k) {
    nums.sort((a, b) => Math.abs(b) - Math.abs(a));
    let res = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] >= 0) {
            res += nums[i];
        }
        else {
            if (k > 0) {
                nums[i] = -nums[i];
                k--;
                res += nums[i];
            }
            else {
                res += nums[i];
            }
        }

    }

    if (k === 0) return res;
    else if (k%2 === 0) return res;
    
    else {
        console.log("?");
        return (res - 2*nums[nums.length-1]);
    }

};