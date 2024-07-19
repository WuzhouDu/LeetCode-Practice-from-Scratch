class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) <= 1):
            return 0
        cur = prices[1] - prices[0]
        result = max(cur, 0)
        for i in range(2, len(prices)):
            difference = prices[i] - prices[i-1]
            cur = max(cur + difference, difference)
            result = max(result, cur)
        return result
