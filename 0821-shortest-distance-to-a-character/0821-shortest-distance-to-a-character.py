class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        ans = []

        for i in range(len(s)):
            min_dist = len(s)

            for j in range(len(s)):
                if s[j] == c:
                    min_dist = min(min_dist, abs(i - j))

            ans.append(min_dist)

        return ans