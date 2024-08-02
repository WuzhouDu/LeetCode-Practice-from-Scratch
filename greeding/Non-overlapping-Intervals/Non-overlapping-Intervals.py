class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if (len(intervals) == 1):
            return 0
        intervals.sort(key = lambda item: item[1])
        pos = intervals[0][1]
        result = 0
        for i in range(1, len(intervals)):
            if (intervals[i][0] < pos):
                result += 1
            else:
                pos = intervals[i][1]
        
        return result