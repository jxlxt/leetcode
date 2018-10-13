#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # this idea is very simple to use binary search to find the first
        # Badversion element, the end condition is left == right
        low, high = 1, n
        while low < high:
            # avoid overflow
            mid = low + (high - mid) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return high
