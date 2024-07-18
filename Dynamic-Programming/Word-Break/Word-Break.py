class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(dp)):
            cur = s[:i]
            for j in wordDict:
                wordLen = len(j)
                if (wordLen > i):
                    continue
                if (cur[-wordLen:] == j):
                    dp[i] = max(dp[i-wordLen], dp[i])
        return dp[-1]