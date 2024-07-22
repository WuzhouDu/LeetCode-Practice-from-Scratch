class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for _ in range(len(text2))]

        for i in range(len(text2)):
            if (text1[0] == text2[i]):
                dp[i] = 1
            elif (i > 0):
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
        
        for i in range(1, len(text1)):
            prevDp = dp[:]
            if (text1[i] == text2[0]):
                dp[0] = 1
            else:
                dp[0] = prevDp[0]
            for j in range(1, len(text2)):
                if (text1[i] == text2[j]):
                    dp[j] = prevDp[j-1] + 1
                else:
                    dp[j] = max(prevDp[j], dp[j-1])

        return dp[-1]