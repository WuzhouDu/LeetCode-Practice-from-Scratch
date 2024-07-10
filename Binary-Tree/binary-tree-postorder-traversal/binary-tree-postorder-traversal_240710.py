# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return []
        
        # recursion
        # result = []
        # result += self.postorderTraversal(root.left)
        # result += self.postorderTraversal(root.right)
        # result.append(root.val)
        # return result

        # iteration
        result = []
        stack = []
        stack.append(root)
        while (stack):
            cur = stack.pop()
            if (cur):
                stack.append(cur)
                stack.append(None)                
                if (cur.right):
                    stack.append(cur.right)
                if (cur.left):
                    stack.append(cur.left)
            else:
                result.append(stack.pop().val)
        
        return result