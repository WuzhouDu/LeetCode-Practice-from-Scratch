# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        left = 0
        right = 0
        cur = root.left
        while (cur):
            cur = cur.left
            left += 1
        cur = root.right
        while (cur):
            cur = cur.left
            right += 1
        if (left == right):
            return (1 << left) + self.countNodes(root.right)
        else:
            return (1 << right) + self.countNodes(root.left)