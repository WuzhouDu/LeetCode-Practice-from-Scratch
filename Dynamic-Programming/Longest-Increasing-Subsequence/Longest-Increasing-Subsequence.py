class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * (len(nums))
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if (nums[i] > nums[j]):
        #             dp[i] = max(dp[j] + 1, dp[i])
        #     # print(dp)
        # return max(dp)

        tail = [nums[0]]
        for i in range(1, len(nums)):
            target = nums[i]
            if (target > tail[-1]):
                tail.append(target)
                continue
            left = 0
            right = len(tail) - 1
            while (left <= right):
                mid = (left + right) // 2
                if (tail[mid] < target):
                    left = mid + 1
                else:
                    right = mid - 1
            tail[left] = target
        return len(tail)
