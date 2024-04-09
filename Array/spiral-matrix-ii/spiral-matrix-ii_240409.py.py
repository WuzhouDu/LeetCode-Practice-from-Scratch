class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        current = 1
        result = []
        for i in range(0, n):
            result.append([j for j in range(0, n)])
        # print(result)
        for i in range(0, (n + 1)/2):
            for first in range(i, n - i - 1):
                result[i][first] = current
                current += 1
            
            for second in range(i, n - i - 1):
                result[second][n-1-i] = current
                current += 1

            for third in range(n - i - 1, i, -1):
                result[n-1-i][third] = current
                current += 1

            for fourth in range(n - i - 1, i, -1):
                result[fourth][i] = current
                current += 1
        if (n % 2):
            result[n/2][n/2] = n * n
        
        return result