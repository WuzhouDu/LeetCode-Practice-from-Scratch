# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return []
        
        # recursion
        # result = []
        # result += self.inorderTraversal(root.left)
        # result.append(root.val)
        # result += self.inorderTraversal(root.right)
        # return result

        # iteration
        result = []
        stack = []
        stack.append(root)
        while (stack):
            cur = stack.pop()
            if (cur):
                if (cur.right):
                    stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if (cur.left):
                    stack.append(cur.left)
            else:
                result.append(stack.pop().val)
        return result