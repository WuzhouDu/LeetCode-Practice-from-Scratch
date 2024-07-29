# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        preSum = 0
        def dfs(root):
            nonlocal preSum
            if (root is None):
                return None
            root.right = dfs(root.right)
            preSum += root.val
            root.val = preSum
            root.left = dfs(root.left)
            return root
        return dfs(root)