class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue  # Skip duplicates

            for j in range(nums[i] + 1, nums[i + 1]):
                result.append(j)

        return result