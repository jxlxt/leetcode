#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:14 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: twoSumIII.py
# @Software: PyCharm


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ctr = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.ctr:
            self.ctr[number] += 1
        else:
            self.ctr[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        ctr = self.ctr
        for num in ctr:
            if value - num in ctr and (value - num != num or ctr[num] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
