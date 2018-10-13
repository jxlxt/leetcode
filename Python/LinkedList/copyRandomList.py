#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/6/18 11:04 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: copyRandomList.py
# @Software: PyCharm

import collections


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = collections.defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        n = head
        while n:
            dic[n].label = n.label
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
