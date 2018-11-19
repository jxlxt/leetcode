class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product, res = 1, []
        # calculate the left side product except self
        for num in nums:
            res.append(product)
            product *= num
        # calculate the right side product except self
        product = 1
        for i in reversed(range(len(nums))):
            res[i] *= product
            product *= nums[i]
        return res
