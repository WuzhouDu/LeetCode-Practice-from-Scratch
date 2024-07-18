class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp = []
        # for i in range(len(strs)):
        #     dp.append([[0 for _ in range(n+1)] for __ in range(m+1)])
        # for i in range(m+1):
        #     if (i < strs[0].count("0")):
        #         continue
        #     for j in range(n+1):
        #         if (j < strs[0].count("1")):
        #             continue
        #         dp[0][i][j] = 1
        
        # for i in range(1, len(strs)):
        #     for j in range(m+1):
        #         for k in range(n+1):
        #             if (j < strs[i].count("0") or k < strs[i].count("1")):
        #                 dp[i][j][k] = dp[i-1][j][k]
        #             else:
        #                 dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j - strs[i].count("0")][k - strs[i].count("1")] + 1)
        # # print(dp)
        # return dp[-1][-1][-1]

        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            if (i < strs[0].count("0")):
                continue
            for j in range(n+1):
                if (j < strs[0].count("1")):
                    continue
                dp[i][j] = 1

        for i in range(1, len(strs)):
            zeroes = strs[i].count("0")
            ones = strs[i].count("1")
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if (j < zeroes or k < ones):
                        continue
                    else:
                        dp[j][k] = max(dp[j][k], dp[j - zeroes][k - ones] + 1)
            
        return dp[-1][-1]