#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/8/18 9:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: maxDepth.py
# @Software: PyCharm
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    """
    So similarly, for a N-ary Tree, instead of comparing depth between only left and right child nodes, we simply iterate all child nodes by (self.maxDepth(node) for node in root.children) and return the max_depth on the current node by the fucntion max(child1, child2, ...). Eventually we will get the maximum depth for the root.
    """

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(node) for node in root.children) + 1
