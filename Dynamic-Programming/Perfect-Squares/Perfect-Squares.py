class Solution:
    def numSquares(self, n: int) -> int:
        perfectSqrs = []
        for i in range(1, n+1):
            if (i*i <= n):
                perfectSqrs.append(i * i)
        
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in perfectSqrs:
            for j in range(i, n+1):
                if (dp[j-i] == -1):
                    continue
                if (dp[j] == -1):
                    dp[j] = dp[j-i] + 1
                else:
                    dp[j] = min(dp[j], dp[j-i] + 1)
                
        return dp[-1]