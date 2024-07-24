class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp
        # dp = [[True for _ in range(len(s))] for __ in range(len(s))]
        # ans = 0
        # for i in range(len(s)):
        #     dp[i][i] = True
        #     ans += 1

        # for i in range(1, len(s)):
        #     for j in range(len(s)-i):
        #         # print(i, j)
        #         if (s[j] == s[i+j]):
        #             dp[j][i+j] = dp[j+1][i+j-1]
        #             if (dp[j][i+j]):
        #                 # print(i, j)
        #                 ans += 1
        #         else:
        #             dp[j][i+j] = False
        # return ans
    
        # expand around center
        # def count(s, l, r):
        #     ans = 0
        #     while (l >= 0 and r <len(s) and s[l] == s[r]):
        #         ans += 1
        #         l -=1
        #         r += 1
        #     return ans

        # result = 0
        # for i in range(len(s)-1):
        #     result += count(s, i, i)
        #     result += count(s, i, i+1)
        
        # result += count(s, len(s) - 1, len(s) - 1)
        # return result

        # Manacher's Algorithm
        new_s = "#" + "#".join(s) + "#"
        n = len(new_s)
        dp = [0] * n
        r = -1
        im = -1
        for i in range(n):
            temp = 0
            if (i < r):
                temp = min(r - i + 1, dp[2 * im - i])
            else:
                temp = 1
            while(i + temp < n and i - temp >= 0 and new_s[i + temp] == new_s[i - temp]):
                temp += 1
            dp[i] = temp
            if (i + temp - 1 > r):
                r = i + temp - 1
                im = i
        return sum(dp[i] // 2 for i in range(n))