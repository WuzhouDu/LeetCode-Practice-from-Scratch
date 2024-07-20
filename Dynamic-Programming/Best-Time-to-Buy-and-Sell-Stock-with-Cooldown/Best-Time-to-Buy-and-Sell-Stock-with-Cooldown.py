class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        elif (len(prices) == 2):
            return max(prices[1] - prices[0], 0)
        
        dp = [[0, 0, 0] for _ in range(len(prices))] 
        dp[0][2] = -prices[0]
        # print(dp)
        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = max(dp[i-1][2] + prices[i], dp[i-1][1])
            dp[i][2] = max(dp[i-1][0] - prices[i], dp[i-1][2])
            # print(dp)
        return max(dp[-1])