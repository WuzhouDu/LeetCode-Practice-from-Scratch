class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [0 for _ in range(m)]
        ans = 0
        for j in range(m):
            if (nums1[0] == nums2[j]):
                dp[j] = 1
                ans = 1

        for i in range(1, n):
            for j in range(m-1, 0, -1):
                if (nums1[i] == nums2[j]):
                    dp[j] = dp[j-1] + 1
                    ans = max(ans, dp[j])
                else:
                    dp[j] = 0
            if (nums1[i] == nums2[0]):
                dp[0] = 1
                ans = max(ans, 1)
            else:
                dp[0] = 0
        return ans