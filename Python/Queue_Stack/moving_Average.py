#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 4:19 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: moving_Average.py
# @Software: PyCharm

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = deque(maxlen=size)
        self.size = size
        self.curSum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.curSum += val
        if len(self.queue) == self.size:
            self.curSum -= self.queue.popleft()
        self.queue.append(val)
        return float(self.curSum) / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)