class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        temp = []
        result = []
        def backtrack(start, target):
            if (target == 0 and len(temp) == k):
                result.append(temp[:])
                return
            if (start > target):
                return
            for i in range(start, 11 - k + len(temp)):
                temp.append(i)
                backtrack(i+1, target-i)
                temp.pop()
        backtrack(1, n)
        return result
