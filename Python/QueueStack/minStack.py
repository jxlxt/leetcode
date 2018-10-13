#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 8:52 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: minStack.py
# @Software: PyCharm


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.items.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items) - 1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items) - 1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()