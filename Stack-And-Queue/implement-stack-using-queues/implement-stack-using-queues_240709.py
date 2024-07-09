class MyStack(object):

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        for _ in range(self.size):
            self.stack.append(self.stack.pop(0))
        self.size += 1

    def pop(self):
        """
        :rtype: int
        """
        self.size -= 1
        return self.stack.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()