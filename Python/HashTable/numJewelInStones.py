#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:11 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: numJewelInStones.py
# @Software: PyCharm


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)
