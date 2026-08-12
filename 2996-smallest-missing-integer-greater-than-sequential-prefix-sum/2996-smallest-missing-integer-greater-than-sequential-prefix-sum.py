class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]

        # Find the longest sequential prefix
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        # Find the smallest integer >= s that is not in nums
        nums_set = set(nums)
        while s in nums_set:
            s += 1

        return s