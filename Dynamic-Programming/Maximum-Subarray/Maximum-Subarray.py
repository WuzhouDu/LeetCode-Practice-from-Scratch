class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        # return max(dp)

        # d and q
        if (len(nums) == 1):
            return nums[0]
        def divideAndConq(l, r):
            if (l>r):
                return (0, 0, 0, 0)
            if (l == r):
                return (nums[l], nums[l], nums[l], nums[l])

            m = (l+r) // 2
            lsum1, rsum1, msum1, asum1 = divideAndConq(l, m)
            lsum2, rsum2, msum2, asum2 = divideAndConq(m+1, r)
            
            lsum = max(lsum1, asum1 + lsum2)
            rsum = max(rsum2, asum2 + rsum1)
            msum = max(msum1, msum2, rsum1 + lsum2)
            asum = asum1 + asum2
            return (lsum, rsum, msum, asum)

        return divideAndConq(0, len(nums)-1)[2]