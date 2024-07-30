class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        result = []
        def backtrack(startIndex, target):
            if (target == 0):
                result.append(temp[:])
                return
            for i in range(startIndex, len(candidates)):
                cur = candidates[i]
                if (cur > target):
                    continue
                temp.append(cur)
                backtrack(i, target - cur)
                temp.pop()
        backtrack(0, target)
        return result