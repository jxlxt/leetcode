#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/8/18 9:55 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: levelOrder.py
# @Software: PyCharm
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelorder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res, stack = [], [root]
        while any(stack):
            res.append([node.val for node in stack])
            stack = [child for node in stack for child in node.children if child]
        return res
