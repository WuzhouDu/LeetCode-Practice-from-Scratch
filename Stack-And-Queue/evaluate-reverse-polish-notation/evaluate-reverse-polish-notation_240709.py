class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if (token == "+"):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif (token == "*"):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif (token == "-"):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif (token == "/"):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        assert(len(stack) == 1)
        return int(stack[0])