# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode()
        dummyHead.next = head
        first = dummyHead
        second = dummyHead
        while (n > 0):
            second = second.next
            n -= 1
        while (second.next != None):
            first = first.next
            second = second.next
        if (first.next):
            first.next = first.next.next
        else:
            first.next = None
        return dummyHead.next