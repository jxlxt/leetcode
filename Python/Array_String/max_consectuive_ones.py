class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 0
        return ans
