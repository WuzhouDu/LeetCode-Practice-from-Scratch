# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = 0

        # return 0 means there is no coverage, 1 means coverage but not placed, 2 means placed a camera
        def dfs(root):
            nonlocal result
            if (root is None):
                return 1
            left = dfs(root.left)
            right = dfs(root.right)
            if (left == 0 or right == 0):
                result += 1
                return 2
            if (left == 2 or right == 2):
                return 1
            if (left == 1 and right == 1):
                return 0
        if (dfs(root) == 0):
            result += 1
        return result