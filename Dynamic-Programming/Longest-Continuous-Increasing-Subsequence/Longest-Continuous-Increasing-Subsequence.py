class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # sliding window
        # left = 0
        # n = len(nums)
        # result = 1
        # while (left < n):
        #     right = left + 1
        #     temp = 1
        #     while (right < n and nums[right] > nums[left]):
        #         temp += 1
        #         left += 1
        #         right += 1
        #     result = max(temp, result)
        #     left += 1
        #     if (right >= n):
        #         break
        # return result

        # dp
        n = len(nums)
        start = 0
        ans = 1
        for i in range(1, n):
            if (nums[i] <= nums[i-1]):
                start = i
            ans = max(ans, i - start + 1)
        return ans