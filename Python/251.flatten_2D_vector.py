#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/23/18 5:19 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: 251.flatten_2D_vector.py
# @Software: PyCharm


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        def get():
            for row in vec2d:
                for elem in row:
                    self.size -= 1
                    yield elem
        self.elem = get()
        self.size = sum(len(row) for row in vec2d)
        print(self.size)

    def next(self):
        """
        :rtype: int
        """
        return next(self.elem)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.size


if __name__ == '__main__':
    vec2d = [[1, 2], [3], [4, 5, 6]]
    i, v = Vector2D(vec2d), []
    while i.hasNext():
        v.append(i.next())
    print(v)