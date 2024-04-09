class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while (left <= right and left >= 0 and right >= 0):
            mid = (left + right) / 2
            if (nums[mid] == target): 
                return mid
            if (nums[mid] > target):
                right = mid - 1
            else: 
                left = mid + 1
            print(mid)
        return -1