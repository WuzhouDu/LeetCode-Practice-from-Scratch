class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        lowerBound = 0
        upperBound = 0
        for i in nums:
            lowerBound -= i
            upperBound += i
        if (target > upperBound or target < lowerBound):
            return 0
        
        # dp = [0] * (upperBound - lowerBound + 1)
        # dp[-lowerBound -nums[0]] += 1
        # dp[-lowerBound +nums[0]] += 1
        # for i in range(1, len(nums)):
        #     # print(dp)
        #     prevDp = dp[:]
        #     for j in range(upperBound - lowerBound + 1):
        #         dp[j] = 0
        #         if (j - nums[i] >= 0):
        #             dp[j] += prevDp[j - nums[i]]
        #         if (j + lowerBound + nums[i] <= upperBound):
        #             dp[j] += prevDp[j + nums[i]]
        # # print(dp)
        # return dp[target-lowerBound]
        total = 0
        for i in nums:
            total += i
        if (target + total) % 2 :
            return 0
        packageTarget = (target + total) // 2
        dp = [0] * (packageTarget + 1)
        for i in range(packageTarget + 1):
            if i == 0:
                dp[i] += 1
            if (i == nums[0]):
                dp[i] += 1
            

        for i in range(1, len(nums)):
        #     print(dp)
            prevDp = dp[:]
            for j in range(packageTarget + 1):
                if (j >= nums[i]):
                    dp[j] += prevDp[j-nums[i]]
        # print(dp)
        return dp[-1]