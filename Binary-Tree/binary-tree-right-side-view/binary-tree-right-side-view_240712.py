# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(root, result, level):
    if (len(result) <= level):
        result.append(root.val)
    if (root.right):
        traverse(root.right, result, level + 1)
    if (root.left):
        traverse(root.left, result, level + 1)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if (not root):
            return result
        result.append(root.val)
        if (root.right):
            traverse(root.right, result, 1)
        if (root.left):
            traverse(root.left, result, 1)
        return result
