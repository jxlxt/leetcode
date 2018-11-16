class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, length, used = [], len(nums), None
        if length == 0: return []
        if length == 1: return [nums]
        for i in range(length):
            if nums[i] == used: continue
            used = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res
