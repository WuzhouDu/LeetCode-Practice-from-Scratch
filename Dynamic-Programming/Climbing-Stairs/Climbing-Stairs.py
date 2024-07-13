class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1
        dp = [1] * 3
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[0], dp[1] = dp[1], dp[2]
            dp[2] = dp[0] + dp[1]
        return dp[2]