#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Time complexity: O(min(a,b)*b)
        # Space complexity: O(1)
        if len(a) == 0: return b
        if len(b) == 0: return a
        # recursive from the last element
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[-1], b[-1]) + '0'
        else:
            return self.addBinary(a[-1], b[-1]) + '1'
