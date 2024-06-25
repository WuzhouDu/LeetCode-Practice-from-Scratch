class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        cur = len(nums) - 1
        while (right >= left):
            leftNum = nums[left]
            rightNum = nums[right]
            if (abs(leftNum) > abs(rightNum)):
                result[cur] = leftNum * leftNum
                cur -= 1
                left += 1
            else:
                result[cur] = rightNum * rightNum
                cur -= 1
                right -= 1
        return result