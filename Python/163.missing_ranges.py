class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums.append(upper+1)
        pre = lower - 1
        for num in nums:
            if num == pre + 2:
                res.append(str(num-1))
            elif num > pre + 2:
                res.append(str(pre+1) + '->' + str(num-1))
            pre = num
        return res
