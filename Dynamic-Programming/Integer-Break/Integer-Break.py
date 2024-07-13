class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            result = i-1 # (i-1) * 1
            for j in range(2, i):
                result = max(result, dp[j] * (i - j), j*(i-j))
            dp[i] = result
        # print(dp)
        return dp[n]