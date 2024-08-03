class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if (len(intervals) == 1):
            return intervals
        result = []
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if (intervals[i][0] <= right):
                right = max(intervals[i][1], right)
            else:
                result.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            if (i == len(intervals)-1):
                result.append([left, right])
        return result