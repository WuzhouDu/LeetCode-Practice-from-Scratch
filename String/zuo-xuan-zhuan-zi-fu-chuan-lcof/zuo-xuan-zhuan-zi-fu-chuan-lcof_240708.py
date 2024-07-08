class Solution(object):
    def dynamicPassword(self, password, target):
        """
        :type password: str
        :type target: int
        :rtype: str
        """
        return password[target:] + password[:target]