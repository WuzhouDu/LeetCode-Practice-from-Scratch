class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0] * (k+1), [0] * (k+1)] for _ in range(len(prices))]
        dp[0][1][0] = -prices[0]
        for i in range(1, k+1):
            dp[0][1][i] = -prices[0]
            dp[0][0][i] = 0

        for i in range(1, len(prices)):
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])
            for j in range(1, k+1):
                dp[i][0][j] = max(dp[i-1][1][j-1] + prices[i], dp[i-1][0][j])
                dp[i][1][j] = max(dp[i-1][1][j], dp[i-1][0][j] - prices[i])
        return max(dp[-1][0])