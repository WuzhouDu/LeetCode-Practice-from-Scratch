class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right = 1
        numsLen = len(nums)
        while (right < numsLen):
            if (nums[right] == nums[right - 1]):
                right += 1
                continue
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left