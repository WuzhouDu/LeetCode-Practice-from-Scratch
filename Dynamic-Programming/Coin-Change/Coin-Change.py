class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in coins:
            for j in range(i, amount + 1):
                if (dp[j] == -1 and dp[j-i] == -1):
                    continue
                elif (dp[j-i] == -1):
                    continue
                elif (dp[j] == -1):
                    dp[j] = dp[j-i] + 1
                else:
                    dp[j] = min(dp[j - i] + 1, dp[j])
        
        return dp[-1]