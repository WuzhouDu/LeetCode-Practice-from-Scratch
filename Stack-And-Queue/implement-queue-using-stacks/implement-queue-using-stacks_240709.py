class MyQueue(object):

    def __init__(self):
        self.inStack = []
        self.outStack = []
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inStack.append(x)
        self.size += 1


    def pop(self):
        """
        :rtype: int
        """
        if (len(self.outStack) == 0):
            while(len(self.inStack) != 0):
                self.outStack.append(self.inStack.pop())
            self.size -= 1
            return self.outStack.pop()
        else:
            self.size -= 1
            return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if (len(self.outStack) == 0):
            while(len(self.inStack) != 0):
                self.outStack.append(self.inStack.pop())
            return self.outStack[-1]
        else:
            return self.outStack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()