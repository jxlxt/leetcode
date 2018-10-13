#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:41 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: inorderTraversal.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # pseudocode
        # iterativeInorder(node)
        # parentStack = empty stack
        # while (not parentStack.isEmpty() or node ≠ null)
        #     if (node ≠ null)
        #         parentStack.push(node)
        #         node = node.left
        #     else
        #         node = parentStack.pop()
        #         visit(node)
        #         node = node.right
        p = root
        stack = []
        ans = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            ans.append(p.val)
            p = p.right
        return ans
