#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:06 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: groupAnagrams.py
# @Software: PyCharm


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for string in strs:
            dic[''.join(sorted(string))] += [string]

        return [value for key, value in dic.items()]
