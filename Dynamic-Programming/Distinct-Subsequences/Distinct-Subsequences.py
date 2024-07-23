class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if (len(t) > len(s)):
            return 0

        dp = [0 for _ in range(len(s))]

        if (t[0] == s[0]):
            dp[0] = 1
        for i in range(1, len(s)):
            if (s[i] == t[0]):
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]

        for i in range(1, len(t)):
            cur = t[i]
            prevDp = dp[:]
            if (t[i] == s[i] and prevDp[i-1] == 1):
                dp[i] = 1
            else:
                dp[i] = 0
            for j in range(i+1, len(s)):
                if (s[j] == cur):
                    dp[j] = prevDp[j-1] + dp[j-1]
                else:
                    dp[j] = dp[j-1]

        return dp[-1]