# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, target):
            if (not root):
                return False
            if (root.left == root.right and root.left is None):
                if (target == root.val):
                    return True
                return False
            if (root.left and dfs(root.left, target - root.val)):
                return True
            if (root.right and dfs(root.right, target - root.val)):
                return True
            return False
        
        return dfs(root, targetSum)