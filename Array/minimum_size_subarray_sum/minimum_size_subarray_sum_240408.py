class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = 0
        result = len(nums)
        current = nums[0]
        while (left < len(nums)):
            if (current < target):
                while (right < len(nums)-1 and current < target):
                    right += 1
                    current += nums[right]
            
            if (current >= target):
                result = min(right-left+1, result)
                left += 1
                current -= nums[left-1]
            else:
                break
        if (current < target and right - left + 1 == len(nums)): return 0
        return result