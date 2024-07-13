class Solution:
    def fib(self, n: int) -> int:
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        table = [0] * 3
        table[1] = 1
        table[2] = 1
        for i in range(3, n+1):
            table[0], table[1] = table[1], table[2]
            table[2] = table[1] + table[0]
        return table[2]