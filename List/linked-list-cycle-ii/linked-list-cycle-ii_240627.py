# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None):
            return None
        dummyHead = ListNode()
        dummyHead.next = head
        fast = dummyHead
        slow = dummyHead

        while (fast != None and slow != None):
            slow = slow.next
            if (fast.next):
                fast = fast.next.next
            else: break

            if (slow == fast):
                temp = dummyHead
                while (temp != slow):
                    temp = temp.next
                    slow = slow.next
                return temp

        return None