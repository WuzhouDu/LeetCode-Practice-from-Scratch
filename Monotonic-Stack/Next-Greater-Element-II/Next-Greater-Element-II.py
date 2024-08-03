class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [-1] * length
        stack = []
        for i in range(length*2):
            index = i % length
            while (stack and nums[stack[-1]] < nums[index]):
                target = stack.pop()
                if (result[target] == -1):
                    result[target] = nums[index]
            stack.append(index)
        
        return result