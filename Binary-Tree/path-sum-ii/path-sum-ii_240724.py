# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum):
            curPath.append(root.val)
            if (root.val == targetSum and root.left == root.right and root.left is None):
                result.append(curPath[:])
                curPath.pop()
                return
            
            if (root.left):
                dfs(root.left, targetSum-root.val)

            if (root.right):
                dfs(root.right, targetSum-root.val)
            curPath.pop()

        result = []
        curPath = []
        if (not root):
            return []
        dfs(root, targetSum)
        return result
