#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = res = 0
        for i, num in enumerate(nums):
            total += num
            while total >= s:
                res = min(res, i-left+1)
                total -= nums[left]
                left += 1
        return res if res <= len(nums) else 0


