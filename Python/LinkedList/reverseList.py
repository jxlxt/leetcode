#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/6/18 10:41 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: reverseList.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iteratively
        # prev = None
        # while head:
        #     curr = head
        #     head = head.next
        #     curr.next = prev
        #     prev = curr
        # return prev

        # recursively
        return self._reverseList(head)

    def _reverseList(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverseList(n, node)
