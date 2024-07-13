class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(m):
            dp.append([1] * n)
        for i in range(n):
            if (i > 0 and dp[0][i-1] == 0):
                dp[0][i] = 0
            elif (obstacleGrid[0][i] == 1):
                dp[0][i] = 0
        for i in range(m):
            if (i > 0 and dp[i-1][0] == 0):
                dp[i][0] = 0
            elif (obstacleGrid[i][0] == 1):
                dp[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if (obstacleGrid[i][j] == 1):
                    dp[i][j] = 0
                else: 
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]