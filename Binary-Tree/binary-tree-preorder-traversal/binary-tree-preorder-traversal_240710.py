# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursion
        if (not root):
            return []
        # result = []
        # result.append(root.val)
        # result += self.preorderTraversal(root.left)
        # result += self.preorderTraversal(root.right)
        # return result

        # iteration
        result = []
        stack = []
        stack.append(root)
        while (stack):
            cur = stack.pop()
            if (cur != None):
                if (cur.right):
                    stack.append(cur.right)
                if (cur.left):
                    stack.append(cur.left)
                stack.append(cur)
                stack.append(None)
            else:
                cur = stack.pop()
                result.append(cur.val)
        return result
