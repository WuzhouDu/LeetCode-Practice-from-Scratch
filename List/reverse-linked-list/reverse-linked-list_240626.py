# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # use recursion
        # if (head == None): return None
        # if (head.next == None):
        #     return head
        # temp = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return temp

        # use iteration
        if (head == None): return None
        cur = None
        nxt = head
        while (nxt != None):
            temp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = temp
        return cur
