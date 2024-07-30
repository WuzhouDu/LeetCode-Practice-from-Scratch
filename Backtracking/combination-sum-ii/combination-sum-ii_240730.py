class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        temp = []
        result = []
        def backtrack(startIndex, target):
            if (target == 0):
                result.append(temp[:])
                return
            for i in range(startIndex, len(candidates)):
                cur = candidates[i]
                if (cur > target):
                    return
                if (i > startIndex and candidates[i] == candidates[i-1]):
                    continue
                temp.append(cur)
                backtrack(i+1, target-cur)
                temp.pop()
            
        backtrack(0, target)
        return result