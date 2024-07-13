# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(root):
    if (not root):
        return (True, 0)
    left = traverse(root.left)
    right = traverse(root.right)
    if (left[0] and right[0]):
        if (abs(left[1] - right[1]) <= 1):
            return (True, max(left[1], right[1]) + 1)
    return (False, -1)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (not root):
            return True

        return traverse(root)[0]