class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) <= 3):
            return max(nums)
        
        # if the first house is not stolen, the same as normal one
        dp1 = [0] * (len(nums))
        dp1[1] = nums[1]
        for i in range(2, len(dp1)):
            dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1])
        
        # if the first house is stolen, then three houses cannot be stolen
        dp2 = [0] * (len(nums) - 2)
        dp2[1] = nums[2]
        for i in range(2, len(dp2)):
            dp2[i] = max(nums[i+1] + dp2[i-2], dp2[i-1])
        
        return max(dp2[-1] + nums[0], dp1[-1])