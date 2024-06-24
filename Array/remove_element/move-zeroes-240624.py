class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        numsLen = len(nums)
        while (right < numsLen):
            if (nums[right] == 0):
                right += 1
                continue
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        while (left < numsLen):
            nums[left] = 0
            left += 1

        return nums