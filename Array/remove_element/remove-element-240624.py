class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        numsLen = len(nums)
        if (numsLen == 0):
            return 0
        left = 0
        right = 0
        while (right < numsLen):
            if (nums[right] == val):
                right += 1
                continue
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left