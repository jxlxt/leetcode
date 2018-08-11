class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        left, right = 0, len(nums) - 1
        whiel left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        
        # for special case, there is only two elements and then compare which
        # one is the maximum
        return left if nums[left] > nums[right] else right
