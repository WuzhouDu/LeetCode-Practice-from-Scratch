class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [[0, 0] for _ in range(len(prices))]
        not_hold = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            prev_not_hold = not_hold
            prev_hold = hold
            not_hold = max(prev_hold + prices[i], prev_not_hold)
            hold = max(prev_not_hold - prices[i], prev_hold)
        return not_hold