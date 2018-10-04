#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:39 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: findMaximumXOR.py
# @Software: PyCharm


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefixs = {num >> i for num in nums}
            ans += any(ans^1^p in prefixs for p in prefixs)
        return ans