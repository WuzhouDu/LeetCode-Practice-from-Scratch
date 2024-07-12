# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, depth):
        result = 10**9
        if (root.left == None and root.right == None):
            return depth
        if (root.left):
            result = min(self.traverse(root.left, depth + 1), result)
        if (root.right):
            result = min(self.traverse(root.right, depth + 1), result)
        return result

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        return self.traverse(root, 1)