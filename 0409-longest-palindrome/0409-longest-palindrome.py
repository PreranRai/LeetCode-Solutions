class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        odd = 0

        for c in set(s):
            n = s.count(c)
            count += (n // 2) * 2

            if n % 2 == 1:
                odd = 1

        return count + odd