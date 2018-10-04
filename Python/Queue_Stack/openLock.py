#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 5:17 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: openLock.py
# @Software: PyCharm


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends: return -1
        queue = ["0000"]
        visits = set(queue + deadends)
        step = 0
        while queue:
            queue0 = []
            for status in queue:
                if status == target: return step
                # start BFS
                for nstatus in self.nextStatus(status):
                    if nstatus in visits:
                        continue
                    visits.add(nstatus)
                    queue0.append(nstatus)
            queue = queue0
            step += 1
        return -1

    def nextStatus(self, status):
        for i, n in enumerate(status):
            for y in (-1, 1):
                # pay attention to the type
                digit = (int(status[i])+y+10)%10
                yield status[:i] + str(digit) + status[i+1:]