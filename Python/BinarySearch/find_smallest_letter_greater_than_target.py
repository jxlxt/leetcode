#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letter[-1] <= target:
            return letters[0]
        
        low, high = 0, len(letters) - 1
        while low < high:
            mid = low + (high - low) // 2
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1
        return letters[low]
