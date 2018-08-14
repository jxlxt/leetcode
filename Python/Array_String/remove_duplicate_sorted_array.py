class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if len(nums) < 2: return len(nums)
        for i in range(1, len(nums)):
            if nums[i] != nums[res]:
                res += 1
                nums[res] = nums[i]
        return res+1

