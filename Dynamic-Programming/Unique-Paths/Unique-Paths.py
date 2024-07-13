class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        col = n - 1
        row = m - 1
        result = 1
        for i in range(col + row, max(col, row), -1):
            result *= i
        for i in range(min(col, row), 0, -1):
            result /= i
        return int(result)