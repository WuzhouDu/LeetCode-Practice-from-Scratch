class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        temp = []
        def backtrack(start, remain):
            if remain == 0:
                result.append(temp[:])
                return
            for i in range(start, n - remain + 2):
                temp.append(i)
                backtrack(i + 1, remain - 1)
                temp.pop()
        backtrack(1, k)
        return result