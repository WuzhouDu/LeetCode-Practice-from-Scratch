class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = 0
        for i in stones:
            total += i
        target = total // 2

        dp = [0] * (target + 1)
        for i in range(target + 1):
            if (i >= stones[0]):
                dp[i] = stones[0]
        
        for i in range(1, len(stones)):
            prevDp = dp[:]
            for j in range(1, target + 1):
                if (j - stones[i] >= 0):
                    dp[j] = max(prevDp[j], prevDp[j - stones[i]] + stones[i])
                else:
                    dp[j] = prevDp[j]
        
        return total - dp[-1] - dp[-1]