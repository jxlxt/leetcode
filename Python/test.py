#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/11/18 11:43 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: test.py
# @Software: PyCharm


nums = [-2, 0, 3, -5, 2, -1]


class NumArray:
    def __init__(self, nums):
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        return self.accu[j + 1] - self.accu[i]


if __name__ == '__main__':
    sol = NumArray(nums)
    param_i = sol.sumRange(0, 2)
    print(param_i)
