#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/23/18 7:08 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: shortestDistance.py
# @Software: PyCharm
import sys
import collections
class Solution:

    def shortestDistance(self, grid):
        row, col = len(grid), len(grid[0])
        dist = [[sys.maxsize for _ in range(col)] for _ in range(row)]
        reachable_count = [[0 for _ in range(col)] for _ in range(row)]
        min_dist = sys.maxsize
        buildings = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    # count the building number and implement BFS
                    self.bfs(i, j, grid, dist, row, col, reachable_count)
                    buildings += 1
        for i in range(row):
            for j in range(col):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxsize else -1

    def bfs(self, i, j, grid, dist, row, col, reachable_count):
        visited = [[False for _ in range(col)] for _ in range(row)]
        visited[i][j] = True
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        q = collections.deque([(i, j, 0)])

        while q:
            i, j, length = q.popleft()
            if dist[i][j] == sys.maxsize:
                dist[i][j] = 0
            dist[i][j] += length
            for dx, dy in directions:
                new_x = i + dx
                new_y = j + dy
                if new_x > -1 and new_x < row and new_y > -1 and new_y < col and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    if grid[new_x][new_y] == 0:
                        q.append((new_x, new_y, length+1))
                        reachable_count[new_x][new_y] += 1


if __name__=='__main__':
    sol = Solution()
    grid = [[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
    print(sol.shortestDistance(grid))