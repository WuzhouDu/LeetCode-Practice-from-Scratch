def checkHappy(n):
    sum = 0
    for num in str(n):
        sum += int(num) * int(num)
    return (sum == 1, sum)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exploredSet = set(())
        while (n not in exploredSet):
            canRet, nextN = checkHappy(n)
            if (canRet):
                return True
            else:
                exploredSet.add(n)
                n = nextN
        
        return False