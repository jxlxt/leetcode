#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pythonic method
        return s[::-1]
        # classic method
        i, j = 0, len(s)-1
        res = list(s)
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return "".join(res)

