class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if (n == 1):
            if (target == nums[0]):
                return 0
            else:
                return -1
            
        else:
            left = 0
            right = n-1
            middle = (left + right) // 2
            while (middle > left):
                if (nums[middle] < target):
                    left = middle + 1
                    middle = (left + right) // 2
                elif (nums[middle] > target):
                    right = middle
                    middle = (left + right) // 2
                else:
                    return middle
            if (nums[middle] == target): return middle
            elif (nums[right] == target): return right
            else: return -1