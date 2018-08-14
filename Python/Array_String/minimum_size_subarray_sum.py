class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = l = res = 0
        for i, num in enumerate(nums):
            total += num
            while total >= s:
                res = min(res, i-l+1)
                total -= nums[left]
                left += 1
        return res if res <= len(nums) else return 0


