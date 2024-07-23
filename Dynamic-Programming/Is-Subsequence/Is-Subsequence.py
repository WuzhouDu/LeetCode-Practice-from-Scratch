class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # double pointers
        # left = 0
        # right = 0
        # while (left < len(s)):
        #     cur = s[left]
        #     while (right < len(t)):
        #         if (t[right] == cur):
        #             right += 1
        #             left += 1
        #             break
        #         else:
        #             right += 1
        #     if right == len(t) and left < len(s):
        #         return False
            
        # return True

        # dp
        if (s == ""):
            return True
        if (len(s) > len(t)):
            return False

        n = len(t)
        dp = [[-1 for _ in range(26)] for __ in range(n)]
        dp[-1][ord(t[-1]) - ord('a')] = n-1
        for i in range(n-2, -1, -1):
            cur = t[i]
            for j in range(ord('a'), ord('z') + 1):
                if (cur == chr(j)):
                    dp[i][j - ord('a')] = i
                else:
                    dp[i][j - ord('a')] = dp[i+1][j - ord('a')]
        
        start = 0
        for i in s:
            if (start >= len(dp)):
                return False
            if (dp[start][ord(i) - ord('a')] != -1):
                start = dp[start][ord(i) - ord('a')] + 1
            else:
                return False
        
        return True
        
