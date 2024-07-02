class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        res = []
        while (s[left] == ' '):
            left += 1
        while (s[right] == ' '):
            right -= 1
        
        word = ""
        while (left <= right):
            if (s[left] != ' '):
                word += s[left]
                left += 1
            else:
                if (word == ""):
                    left += 1
                else:
                    res.append(word)
                    word = ""
                    left += 1
        res.append(word)

        res.reverse()
        return " ".join(res)


     