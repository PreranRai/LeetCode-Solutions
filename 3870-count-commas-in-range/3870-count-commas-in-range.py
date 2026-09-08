class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        divisor = 1000

        while divisor <= n:
            count += n - divisor + 1
            divisor *= 1000

        return count