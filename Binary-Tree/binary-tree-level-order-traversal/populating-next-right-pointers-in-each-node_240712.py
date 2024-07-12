"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if (not root):
            return root
        cur = root
        while (cur.left):
            hook = cur.left
            cur.left.next = cur.right
            while (cur.next):
                cur.right.next = cur.next.left
                cur = cur.next
                cur.left.next = cur.right
            cur = hook
        
        return root