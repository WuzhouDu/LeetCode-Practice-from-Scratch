class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        result = [[0 for _ in range(n)] for _ in range(n)]
        cur = 1
        while (left <= right and top <= bottom):
            for i in range(left, right+1):
                result[top][i] = cur
                cur += 1
            top += 1
            if (top > bottom): break

            for i in range(top, bottom+1):
                result[i][right] = cur
                cur += 1
            right -= 1
            if (left > right): break

            for i in range(right, left - 1, -1):
                result[bottom][i] = cur
                cur += 1
            bottom -= 1
            if (top > bottom): break

            for i in range(bottom, top - 1, -1):
                result[i][left] = cur
                cur += 1
            left += 1
            if (left > right): break

        return result