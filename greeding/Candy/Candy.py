class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1] * len(ratings)
        result = 0
        for i in range(1, len(ratings)):
            if (ratings[i] > ratings[i-1]):
                left[i] = left[i-1] + 1
        
        for i in range(len(ratings)-1, 0, -1):
            if (ratings[i-1] > ratings[i]):
                left[i-1] = max(left[i] + 1, left[i-1])
            result += left[i]
        result += left[0]
        return result