#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 5:53 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: singleNumber.py
# @Software: PyCharm


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key
