# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l, r):
            if (l==r):
                return TreeNode(nums[l])
            if (l > r):
                return None
            maxI = -1
            maxVal = -1
            for i in range(l, r+1):
                if nums[i] > maxVal:
                    maxVal = nums[i]
                    maxI = i
            
            root = TreeNode(maxVal)
            root.left = build(l, maxI-1)
            root.right = build(maxI+1, r)
            return root
        return build(0, len(nums)-1)