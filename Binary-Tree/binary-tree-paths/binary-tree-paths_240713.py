# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def recur(curPath, root):
            if (not root):
                return
            curPath += "->" + str(root.val)
            if (root.left == None and root.right == None):
                result.append(curPath)
                return
            recur(curPath, root.left)
            recur(curPath, root.right)

        result = []
        cur = str(root.val)
        if (root.left == None and root.right == None):
            result.append(cur)
            return result
        recur(cur, root.left)
        recur(cur, root.right)
        return result