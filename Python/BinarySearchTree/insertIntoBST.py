#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 10:52 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: insertIntoBST.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root and root.val > val and not self.insertIntoBST(root.left, val):
            root.left = TreeNode(val)
        elif root and root.val < val and not self.insertIntoBST(root.right, val):
            root.right = TreeNode(val)
        return root
