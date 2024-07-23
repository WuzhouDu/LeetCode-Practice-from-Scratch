class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[True for _ in range(len(s))] for __ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            dp[i][i] = True
            ans += 1

        for i in range(1, len(s)):
            for j in range(len(s)-i):
                # print(i, j)
                if (s[j] == s[i+j]):
                    dp[j][i+j] = dp[j+1][i+j-1]
                    if (dp[j][i+j]):
                        # print(i, j)
                        ans += 1
                else:
                    dp[j][i+j] = False
        

        return ans