def getHelp(needle):
    if (len(needle) <= 2):
        return [0, 0]
    result = [0] * len(needle)
    for i in range(2, len(needle)):
        prev = needle[i-1]
        prevMatch = result[i-1]
        if (needle[prevMatch] == prev):
            result[i] = result[i-1] + 1
        else:
            while (prevMatch != 0):
                prevMatch = result[prevMatch]
                if (needle[prevMatch] == prev):
                    result[i] = prevMatch + 1
                    break
                    
            if (prevMatch == 0):
                result[i] = 1 if needle[0] == prev else 0
    # print(result)
    return result

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        helpArray = getHelp(needle)
        hayPtr = 0
        needlePtr = 0
        while (hayPtr < len(haystack)):
            if (haystack[hayPtr] == needle[needlePtr]):
                if (needlePtr == len(needle) - 1):
                    return hayPtr - len(needle) + 1
                hayPtr += 1
                needlePtr += 1
                continue
            elif (needlePtr == 0):
                hayPtr += 1
            else:
                needlePtr = helpArray[needlePtr]
                
        return -1