#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # find the closest element and set right pointer as the index of
        # closest index
        left, right, res = 0, len(arr) - 1, []
        while(left < right):
            mid = left + (right - left) // 2
            if arr[mid] == x:
                right = mid
                break
            elif arr[mid] > x:
                right = mid - 1
            else:
                left = mid - 1

        # ensure the range
        left = right
        while right - left < k:
            if left == 0: return arr[k]
            if right == len(arr): return arr[-k:]
            if x - arr[left - 1] < arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left:right]
