#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:02 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: findRestaurant.py
# @Software: PyCharm


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index = {u: i for i, u in enumerate(list1)}
        best, ans = 1e9, []

        for j, v in enumerate(list2):
            i = index.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans
