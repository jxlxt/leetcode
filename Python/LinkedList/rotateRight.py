#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/6/18 11:05 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: rotateRight.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next == None:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1

        rotateTimes = k % length

        if k == 0 or rotateTimes == 0:
            return head

        fast = slow = head

        for a in range(rotateTimes):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        temp = slow.next
        slow.next = None
        fast.next = head
        head = temp

        return head
