# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (not root):
            return []
        result = []
        queue = []
        queue.append(root)
        level = 0
        while (queue):
            curAmount = len(queue)
            result.append([])
            for i in range(curAmount):
                cur = queue[i]
                result[level].append(cur.val)
                if (cur.left):
                    queue.append(cur.left)
                if (cur.right):
                    queue.append(cur.right)
            level += 1
            queue = queue[curAmount:]
        return result