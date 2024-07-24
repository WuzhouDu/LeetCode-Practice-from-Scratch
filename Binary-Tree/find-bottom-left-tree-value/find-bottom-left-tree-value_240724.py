# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        res = 0
        q.append(root)
        while (q):
            n = len(q)
            res = q[0].val
            for i in range(n):
                cur = q.popleft()
                if (cur.left):
                    q.append(cur.left)
                if (cur.right):
                    q.append(cur.right)
        return res