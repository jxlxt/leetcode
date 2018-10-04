#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 4:21 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: walls_Gates.py
# @Software: PyCharm

from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        queue = deque()

        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        dis = 0
        while queue:
            length = len(queue)
            dis += 1
            for i in  range(length):
                cur = queue.popleft()
                for dir in dirs:
                    nextPos = (cur[0] + dir[0], cur[1] + dir[1])
                    if nextPos[0] >= 0 and nextPos[0] < m and nextPos[1] >= 0 and nextPos[1] < n and rooms[nextPos[0]][nextPos[1]] == 2147483647:
                        rooms[nextPos[0]][nextPos[1]] = dis
                        queue.append(nextPos)