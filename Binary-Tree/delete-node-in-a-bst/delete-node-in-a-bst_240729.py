# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delete(self, root):
        if (root.right):
            cur = root.right
            while (cur.left):
                cur = cur.left
            cur.left = root.left
            return root.right
        else:
            return root.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if (root is None):
            return root
        cur = root
        parent = None
        while (cur):
            if (cur.val > key):
                parent = cur
                cur = cur.left
            elif (cur.val < key):
                parent = cur
                cur = cur.right
            else:
                if (parent is None):
                    return self.delete(cur)
                elif parent.left == cur:
                    parent.left = self.delete(cur)
                else:
                    parent.right = self.delete(cur)
                return root
        return root