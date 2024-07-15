class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0
        curMax = 0
        for i in nums:
            totalSum += i
            curMax = max(curMax, i)
        if (totalSum % 2):
            return False
        targetSum = totalSum // 2
        if (curMax > targetSum):
            return False
        if (curMax == targetSum):
            return True

        # dp = [False] * (targetSum+1)
        # for i in range(len(nums)):
        #     dp[i] = [False] * (targetSum+1)
        # for i in range(targetSum + 1):
        #     dp[0][i] = (i == 0 or i == nums[0])
        # for i in range(len(nums)):
        #     dp[i][0] = True
        
        # for i in range(1, len(nums)):
        #     for j in range(1, targetSum + 1):
        #         if (dp[i-1][j]):
        #             dp[i][j] = True
        #         elif (dp[i-1][j-nums[i]]):
        #             dp[i][j] = True
        #         else:
        #             dp[i][j] = False
        # return dp[-1][-1]

        dp = [False] * (targetSum + 1)
        dp[0] = dp[nums[0]] = True
        for i in range(1, len(nums)):
            prevDP = dp[:]
            for j in range(1, targetSum + 1):
                if (prevDP[j]):
                    dp[j] = True
                elif ((j-nums[i] >= 0) and prevDP[j-nums[i]]):
                    dp[j] = True
                else:
                    dp[j] = False
        return dp[-1]