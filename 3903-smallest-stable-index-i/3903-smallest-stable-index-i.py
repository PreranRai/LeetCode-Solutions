class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            left_max = max(nums[:i + 1])
            right_min = min(nums[i:])

            if left_max - right_min <= k:
                return i

        return -1