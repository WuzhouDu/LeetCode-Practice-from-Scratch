class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0 for _ in range(1+len(word2))]
        # for i in range(1, 1+len(word1)):
        #     dp[i][0] = i
        for i in range(1, 1+len(word2)):
            dp[i] = i
        # print("init")
        # print(dp)
        # print("begin dp")
        # print(dp[0])
        for i in range(1, len(word1) + 1):
            prevDp = dp[:]
            dp[0] = i
            for j in range(1, len(word2) + 1):
                if (word1[i-1] == word2[j-1]):
                    dp[j] = prevDp[j-1]
                else:
                    dp[j] = min(prevDp[j], dp[j-1]) + 1
            # print(dp[i])
        
        return dp[-1]