class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapS = {}
        for element in s:
            if (mapS.get(element) == None):
                mapS[element] = 1
            else:
                mapS[element] += 1
        
        for element in t:
            if (mapS.get(element) == None):
                return False
            else:
                mapS[element] -= 1
                if (mapS[element] == 0):
                    del mapS[element]
        
        if (len(mapS) == 0):
            return True
        else:
            return False
