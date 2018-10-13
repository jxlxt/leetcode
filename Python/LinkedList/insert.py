#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/6/18 11:02 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: insert.py
# @Software: PyCharm


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        # check whether exists a cyclic LinkList
        if not head:
            result = Node(insertVal, None)
            result.next = result
            return result
        curr = head
        n = curr.next
        while n:
            insert = False
            # check for four situations
            if insertVal > curr.val > n.val:
                insert = True
            elif insertVal < n.val < curr.val:
                insert = True
            elif n is head:
                insert = True
            elif curr.val <= insertVal <= n.val:
                insert = True
            if insert:
                new = Node(insertVal, n)
                curr.next = new
                return head
            curr = curr.next
            n = curr.next
