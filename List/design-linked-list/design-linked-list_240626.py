class MyListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if (index > self.length - 1 or index < 0):
            return -1
        cur = self.head
        while (index > 0):
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = MyListNode(val)
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
            self.length = 1
            return
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = MyListNode(val)
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
            self.length = 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if (index > self.length or index < 0):
            return
        newNode = MyListNode(val)
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
            self.length = 1
            return
        if (index == 0):
            newNode.next = self.head
            self.head = newNode

        elif (index == self.length):
            self.tail.next = newNode
            self.tail = newNode

        else:
            cur = self.head
            while (index > 1):
                cur = cur.next
                index -= 1
            newNode.next = cur.next
            cur.next = newNode
        self.length += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if (index < 0 or index > self.length - 1):
            return
        if (index == 0):
            self.head = self.head.next
        else:
            cur = self.head
            while (index > 1):
                cur = cur.next
                index -= 1
            if (cur.next != self.tail):
                cur.next = cur.next.next
            else:
                cur.next = None
                self.tail = cur

        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)