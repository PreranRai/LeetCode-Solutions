class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []

        for n in range(left, right + 1):
            x = n
            while x:
                digit = x % 10

                if digit == 0 or n % digit != 0:
                    break

                x //= 10
            else:
                ans.append(n)

        return ans