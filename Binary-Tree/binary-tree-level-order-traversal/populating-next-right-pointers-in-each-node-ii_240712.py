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
    def connect(self, root: 'Node') -> 'Node':
        if (not root):
            return root
        head = root
        while (head):
            dummy = Node()
            temp = dummy
            cur = head
            while (cur):
                if (cur.left):
                    temp.next = cur.left
                    temp = temp.next
                if (cur.right):
                    temp.next = cur.right
                    temp = temp.next
                cur = cur.next
            head = dummy.next
        return root