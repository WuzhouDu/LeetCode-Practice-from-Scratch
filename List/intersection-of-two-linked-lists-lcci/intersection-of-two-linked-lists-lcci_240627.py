# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA == None or headB == None):
            return None

        dummyA = ListNode()
        dummyA.next = headA
        dummyB = ListNode()
        dummyB.next = headB

        ptrA = dummyA
        ptrB = dummyB

        while(ptrA and ptrB):
            if (ptrA == ptrB):
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
        
        if (ptrA == None and ptrB == None):
            return None
        if (ptrA == None):
            ptrA = headB
        else:
            ptrB = headA
        
        while(ptrA and ptrB):
            if (ptrA == ptrB):
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
        if (ptrA == None):
            ptrA = headB
        else:
            ptrB = headA
        
        while(ptrA and ptrB):
            if (ptrA == ptrB):
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
        
        return None
