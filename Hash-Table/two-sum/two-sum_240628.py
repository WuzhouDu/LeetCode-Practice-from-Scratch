class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        matchMap = {}
        for i in range(len(nums)):
            current = nums[i]
            need = target - current
            if (need in matchMap):
                return [matchMap[need], i]
            matchMap[current] = i