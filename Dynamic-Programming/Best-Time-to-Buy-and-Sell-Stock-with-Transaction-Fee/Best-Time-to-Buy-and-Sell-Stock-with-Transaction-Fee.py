class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [0, -prices[0]]
        for i in range(1, len(prices)):
            prevDP = dp[:]
            dp[0] = max(prevDP[0], prevDP[1] + prices[i] - fee)
            dp[1] = max(prevDP[1], prevDP[0] - prices[i])
        
        return dp[0]
        