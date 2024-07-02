class Solution(object):
    def pathEncryption(self, path):
        """
        :type path: str
        :rtype: str
        """
        sList = list(path)
        for i in range(len(sList)):
            if (sList[i] == "."):
                sList[i] = " "
        
        return "".join(sList)
