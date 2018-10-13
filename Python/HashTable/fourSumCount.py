#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:15 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: fourSumCount.py
# @Software: PyCharm

import collections


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)
