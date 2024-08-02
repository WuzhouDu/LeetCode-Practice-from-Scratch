class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if (len(points) == 1):
            return 1
        points.sort(key= lambda item: item[1])
        pos = points[0][1]
        result = 1
        for i in range(1, len(points)):
            if (points[i][0] <= pos):
                continue
            pos = points[i][1]
            result += 1
        return result