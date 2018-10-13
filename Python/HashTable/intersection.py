#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 5:53 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: intersection.py
# @Software: PyCharm


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
