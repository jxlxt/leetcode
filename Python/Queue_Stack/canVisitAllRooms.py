#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:24 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: canVisitAllRooms.py
# @Software: PyCharm


class Solution:
    visited = set()

    def dfs(self, i, rooms):
        if i not in self.visited:
            self.visited.add(i)
            for j in rooms[i]:
                self.dfs(j, rooms)

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.visited = set()
        self.dfs(0, rooms)
        return len(self.visited) == len(rooms)