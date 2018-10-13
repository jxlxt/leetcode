#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # check for corner case
        if not strs: return ""
        # main idea is to use zip() and set to get the common prefix of strs
        # and for different length, in python we use *strs to ignore the
        # limitation
        for i, value in enumerate(zip(*strs)):
            if len(zip(value)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
