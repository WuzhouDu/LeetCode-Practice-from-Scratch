class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if (k == 1):
            return s
        i = 0
        n = len(s)
        sList = list(s)
        while (i < n):
            left = i
            right = min(i + k - 1, n - 1)
            while (left < right):
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
            i += 2 * k
        
        return "".join(sList)