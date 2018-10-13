#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/6/18 10:45 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: removeElements.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        cur = head
        cur_next = cur.next

        while cur_next:
            if cur_next.val == val:
                cur_next = cur_next.next
                cur.next = cur_next
            else:
                cur = cur_next
                cur_next = cur_next.next

        if head.val == val:
            head = head.next

        return head
