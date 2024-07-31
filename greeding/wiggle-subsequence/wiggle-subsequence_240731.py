class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if (len(nums) < 2):
            return len(nums)
        
        down = 1
        up = 1
        for i in range(1, len(nums)):
            if (nums[i] > nums[i-1]):
                up = max(down + 1, up)
            elif (nums[i] < nums[i-1]):
                down = max(up + 1, down)
        
        return max(up, down)