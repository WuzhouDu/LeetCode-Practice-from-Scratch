class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for element in s:
            if (stack and stack[-1] == element):
                stack.pop()
            else:
                stack.append(element)
        
        return "".join(stack)