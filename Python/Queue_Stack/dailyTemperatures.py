#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 9:00 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: dailyTemperatures.py
# @Software: PyCharm


class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        T, ans, stack = temperatures, [0]*len(T), []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans