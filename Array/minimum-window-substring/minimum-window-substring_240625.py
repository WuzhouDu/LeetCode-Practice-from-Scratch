def check(remainMap):
    for val in remainMap.values():
        if (val > 0):
            return False
    return True
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        right = 0
        remainMap = {}
        result = ""
        curMin = len(s) + 1
        for char in t:
            if (remainMap.get(char) != None):
                remainMap[char] += 1
            else:
                remainMap[char] = 1
        
        while (right < len(s)):
            if (remainMap.get(s[right]) != None):
                remainMap[s[right]] -= 1
                right += 1
                if (check(remainMap)):
                    if (curMin > right - left):
                        curMin = right - left
                        result = s[left : right]
                    while (left < right):
                        if (remainMap.get(s[left]) != None):
                            if (check(remainMap)):
                                if (curMin > right - left):
                                    curMin = right - left
                                    result = s[left : right]
                            remainMap[s[left]] += 1
                            if (check(remainMap)):
                                left += 1
                                if (curMin > right - left):
                                    curMin = right - left
                                    result = s[left : right]
                            else:
                                remainMap[s[left]] -= 1
                                break
                        else:
                            left += 1
                    
            else:
                right += 1
        return result