class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sPtr = len(s) - 1
        tPtr = len(t) - 1
        while (sPtr >= 0 or tPtr >= 0):
            sSkip = 0
            while(sPtr >= 0):
                if (s[sPtr] == "#"):
                    sSkip += 1
                    sPtr -= 1
                elif (sSkip == 0):
                    break
                else:
                    sSkip -= 1
                    sPtr -= 1
            tSkip = 0
            while(tPtr >= 0):
                if (t[tPtr] == "#"):
                    tSkip += 1
                    tPtr -= 1
                elif (tSkip == 0):
                    break
                else:
                    tSkip -= 1
                    tPtr -= 1
            if (sPtr >= 0 and tPtr >= 0):
                if (s[sPtr] != t[tPtr]):
                    return False
            elif (sPtr >= 0 or tPtr >= 0):
                return False
            sPtr -= 1
            tPtr -= 1

        return True