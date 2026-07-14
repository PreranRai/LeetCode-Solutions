class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.index(s[i]) == s.rindex(s[i]):
                return i
        return -1