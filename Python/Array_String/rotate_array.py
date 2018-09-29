#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        A little important thing to be cautious:

        nums[:] = nums[n-k:] + nums[:n-k]
        can't be written as:

        nums = nums[n-k:] + nums[:n-k]
        on the OJ.

        The previous one can truly change the value of old nums, but the following one just changes its reference to a new nums not the value of old nums.
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[-k:]+nums[:-k]

