class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_ = 0
        for i in range(len(nums)):
            if i > max_:
                return False
            else:
                max_ = max(nums[i]+i, max_)
        return True


if __name__ == '__main__':
    nums = [3,2,1,0,4]
    sol = Solution()
    print(sol.canJump(nums))
