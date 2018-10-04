#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 7:47 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: stackQueue.py
# @Software: PyCharm

import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._quque = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self._quque
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._quque.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._quque[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._quque) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()