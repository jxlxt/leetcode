#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/8/18 9:54 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: preorder.py
# @Software: PyCharm
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res, q = [], root and [root]
        while q:
            node = q.pop()
            res.append(node.val)
            q += [child for child in node.children[::-1] if child]
        return res
