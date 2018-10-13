#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.items = [None]*k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.items[0] = value
            self.head = 0
            self.tail = 0
            return True
        else:
            self.tail = (self.tail + 1) % self.size
            self.items[self.tail] = value
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.items[self.head] = None
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.size
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.items[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.items[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.head == -1 and self.tail == -1

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.head == (self.tail + 1) % self.size
