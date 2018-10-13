#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 5:50 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: containsDuplicate.py
# @Software: PyCharm


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
