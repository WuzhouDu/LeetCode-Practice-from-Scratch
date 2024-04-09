class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if (nums == []):
            return 0
        left = 0
        right = len(nums) - 1
        while (right >= 0 and nums[right] == val):
            right -= 1

        while (left <= right):
            if (nums[left] == val):
                nums[left],nums[right] = nums[right], nums[left]
                right -= 1
                while (right >= 0 and nums[right] == val):
                    right -= 1
            left += 1
        return right + 1