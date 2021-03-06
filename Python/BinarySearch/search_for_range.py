#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def findMin(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """

        # search from the left side
        res = [-1, -1]
        if nums is None or len(nums) == 0:
            return res
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return res
        else:
            res[0] = left

        # search from the right side
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        res[1] = right
        return res
