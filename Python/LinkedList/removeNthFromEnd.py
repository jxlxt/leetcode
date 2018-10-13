#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/6/18 10:40 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: removeNthFromEnd.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head