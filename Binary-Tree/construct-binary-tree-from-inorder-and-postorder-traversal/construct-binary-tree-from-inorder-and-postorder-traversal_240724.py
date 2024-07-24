# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inl, inr, postl, postr):
            if (inl == inr):
                return TreeNode(inorder[inl])
            if (inl > inr):
                return None
            if (postr > len(postorder)-1):
                return None
            rootVal = postorder[postr]
            rootI = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.left = build(inl, rootI-1, postl, postl + rootI-1-inl)
            leftAmt = max(0, rootI-inl)
            rightAmt = inr - inl - leftAmt
            root.right = build(rootI+1, inr, postr-rightAmt, postr-1)

            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder)-1)
