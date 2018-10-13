#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

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
            # we will use '//' rather than '/' because we want to get the
            # floored value
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return
