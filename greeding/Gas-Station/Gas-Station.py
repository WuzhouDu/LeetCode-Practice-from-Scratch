class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        begin = 0
        while (begin < n):
            i = begin
            res = gas[i % n] - cost[i % n]
            while (res >= 0 and i < begin + n):
                i += 1
                res += gas[i % n] - cost[i % n]
            if (i == begin + n):
                return begin
            elif i == begin:
                begin += 1
            else:
                begin = i
        return -1
