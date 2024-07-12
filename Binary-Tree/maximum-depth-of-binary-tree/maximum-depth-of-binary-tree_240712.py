# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, depth):
        left = depth
        right = depth
        if (root.left):
            left = self.traverse(root.left, depth + 1)
        if (root.right):
            right = self.traverse(root.right, depth + 1)
        return max(left, right)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        return self.traverse(root, 1)