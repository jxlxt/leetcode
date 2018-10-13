#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:03 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: findUniqChar.py
# @Software: PyCharm


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
