class Solution:
    '''
    Idea:
    first, we need to create two pointer, one is at the first element of nums
    and the second is at the end of the nums. Everytime we will calculate the
    mid elements in nums and compare with the target, if mid is smaller than
    the target, we should add left, otherwise we should decrease the right
    value. What's more, if after iteration, we cannot find the target index, we
    will return -1.
    Time complexity: O(logN)
    Space complexity: O(1)
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return 
        
