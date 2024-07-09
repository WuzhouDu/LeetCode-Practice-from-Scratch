class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for element in s:
            if (element == "(" or element == "{" or element == "["):
                stack.append(element)
            elif (element == ")"):
                if (stack and stack[-1] == "("):
                    stack.pop()
                else:
                    return False
            elif (stack and element == "}"):
                if (stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
            else:
                if (stack and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0