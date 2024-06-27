# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None): 
            return head
        dummyHead = ListNode()
        dummyHead.next = head
        first = head
        second = head.next
        cur = dummyHead
        while(first and second):
            cur.next = second
            temp = second.next
            second.next = first
            first.next = temp
            cur = first
            first = temp
            if (first):
                second = first.next
        return dummyHead.next