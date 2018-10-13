#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 10:24 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: levelOrder.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, stack = [], [root]
        while stack:
            ans.append([node.val for node in stack])
            temp = []
            for node in stack:
                temp.extend([node.left, node.right])
