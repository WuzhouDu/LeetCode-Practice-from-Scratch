class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newIndex = 0
        index = 0
        end = False
        while (index < len(nums)):
            val = nums[index]
            nums[newIndex] = val
            while (index < len(nums)-1):
                if (index == len(nums)-2 and nums[index] == nums[index+1]):
                    end = True
                if (nums[index] != nums[index+1]):
                    break
                index += 1
            if (end): break
            index += 1
            newIndex += 1
        if (end): return newIndex+1
        else: return newIndex