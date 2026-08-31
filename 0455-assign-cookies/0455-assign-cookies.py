class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = 0

        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                i += 1

        return i