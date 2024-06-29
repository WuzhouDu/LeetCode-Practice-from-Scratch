class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if (len(nums) < 4):
            return result
        nums.sort()
        n = len(nums)
        iLen = n - 3
        jLen = n - 2
        for i in range(iLen):
            if nums[i]>target and nums[i]>0 and target>0:
                break
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[iLen] + nums[jLen] + nums[n - 1] < target:
                continue
            for j in range(i + 1, jLen):
                if nums[i]+nums[j]>target and target>0:
                    break
                if (j > i+1 and nums[j] == nums[j-1]):
                    continue

                left = j + 1
                right = n - 1

                while (left < right):
                    while (left > j+1 and nums[left] == nums[left - 1] and left < right):
                        left += 1
                    while (right < n-1 and nums[right] == nums[right + 1] and left < right):
                        right -= 1
                    if (left < right):
                        _sum = nums[i] + nums[j] + nums[left] + nums[right]
                        if (_sum > target):
                            right -= 1
                        elif _sum < target:
                            left += 1
                        else:
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            right -= 1
        
        return result