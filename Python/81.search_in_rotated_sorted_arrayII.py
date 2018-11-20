# a good explaination of this problem
# https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51602234
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums is None: return False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            # the first half is ordered
            elif nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:                 
                    left = mid + 1
            # the second half is ordered
            elif nums[left] > nums[mid]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # triky part
            else:
                left += 1
        return False
