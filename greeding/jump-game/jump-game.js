/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    if (nums.length === 1) return true;
    let current = 0;
    let cover = current + nums[current];
    while (current <= cover) {
        if (cover >= nums.length-1) return true;
        cover = Math.max(current + nums[current], cover);
        current++;
    }
    return false;
};