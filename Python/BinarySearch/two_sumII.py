#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # the first method is dictinoary method
        dict = {}
        # enumerate() get the index and value of array
        for i, num in enumerate(numbers):
            if target - num in dict:
                return [dict[target-num]+1, i+1]
            dict[num] = i

        # binary search method
        for i in range(len(numbers)):
            left, right = i+1, len(numbers) - 1
            res = target - numbers[i]
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == res:
                    return [i+1, mid+1]
                elif numbers[mid] < res:
                    left = mid + 1
                else:
                    right = mid - 1

