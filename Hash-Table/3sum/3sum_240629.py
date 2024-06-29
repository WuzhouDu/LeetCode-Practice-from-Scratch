class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            target = - nums[i]
            if (target < 0):
                return result
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            target = - nums[i]
            left = i + 1
            right = len(nums) - 1

            if (nums[i] + nums[i + 1] + nums[i + 2] > 0):
                break
            if (nums[i] + nums[right] + nums[right - 1] < 0):
                continue
            while (left < right):
                if (left > i + 1 and nums[left] == nums[left - 1]):
                    left += 1
                    continue
                if (right < len(nums) - 1 and nums[right] == nums[right+1]):
                    right -= 1
                    continue
                if (nums[left] + nums[right] > target):
                    right -= 1
                elif (nums[left] + nums[right] < target):
                    left += 1
                else:
                    result.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1


        return result