class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        left = [-1] * n
        right = [-1] * n
        leftMax = -1
        for i in range(1, n):
            if (height[i-1] > leftMax):
                left[i] = height[i-1]
                leftMax = height[i-1]
            else:
                left[i] = leftMax
        rightMax = -1
        for i in range(n-2, -1, -1):
            if (height[i+1] > rightMax):
                right[i] = height[i+1]
                rightMax = height[i+1]
            else:
                right[i] = rightMax
        
        for i in range(1, n-1):
            curHeight = height[i]
            curLeftMax = left[i]
            curRightMax = right[i]
            if (curLeftMax > curHeight and curRightMax > curHeight):
                result += min(curLeftMax, curRightMax) - curHeight
        return result