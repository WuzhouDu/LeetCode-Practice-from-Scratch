class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        nextGreater = [-1] * len(nums2)
        stack = []
        for i in range(len(nums2)):
            while (stack and nums2[stack[-1]] < nums2[i]):
                index = stack.pop()
                nextGreater[index] = nums2[i]
            stack.append(i)
        for i in range(len(nums1)):
            result[i] = nextGreater[nums2.index(nums1[i])]
        return result