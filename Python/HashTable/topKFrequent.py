#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:16 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: topKFrequent.py
# @Software: PyCharm


import collections


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
