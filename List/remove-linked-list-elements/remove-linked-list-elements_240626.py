# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while (cur != None):
            if (cur.next != None):
                if (cur.next.val == val):
                    cur.next = cur.next.next
                    continue
                else:
                    cur = cur.next
            else:
                cur = cur.next
        return dummy.next