# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (not root):
            return []
        result = []
        queue = []
        queue.append(root)
        while (queue):
            amt = len(queue)
            curLevel = []
            for i in range(amt):
                cur = queue[i]
                if (cur.left):
                    queue.append(cur.left)
                if (cur.right):
                    queue.append(cur.right)
                curLevel.append(cur.val)
            queue = queue[amt:]
            result.append(curLevel)
        result.reverse()
        return result