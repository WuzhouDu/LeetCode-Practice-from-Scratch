class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        result = len(nums) + 1
        curSum = 0
        for right in range(1, len(nums) + 1):
            curSum += nums[right - 1]
            while (left < right):
                if (curSum >= target):
                    result = min(result, right - left)
                else: 
                    break
                curSum -= nums[left]
                left += 1

        if (result == len(nums) + 1): return 0
        return result