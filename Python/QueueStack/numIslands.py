#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 4:34 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: numIslands.py
# @Software: PyCharm

class Solution(object):
    def isValid(self, r, c, grid):
        row, column = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= row or c >= column:
            return False
        return True

    # BFS solution
    # def bfs(self, r, c, grid):
    #     neighbours = deque()
    #     neighbours.append((r, c))
    #     grid[r][c] = '0'
    #     while neighbours:
    #         row, col = neighbours.popleft()
    #         if self.isValid(row-1, col, grid) and grid[row-1][col] == '1':
    #             neighbours.append((row-1, col))
    #             grid[row-1][col] = '0'
    #         if self.isValid(row+1, col, grid) and grid[row+1][col] == '1':
    #             neighbours.append((row+1, col))
    #             grid[row+1][col] = '0'
    #         if self.isValid(row, col-1, grid) and grid[row][col-1] == '1':
    #             neighbours.append((row, col-1))
    #             grid[row][col-1] = '0'
    #         if self.isValid(row, col+1, grid) and grid[row-1][col+1] == '1':
    #             neighbours.append((row, col+1))
    #             grid[row][col+1] = '0'

    # DFS solution
    def dfs(self, r, c, grid):
        grid[r][c] = '0'
        dirs = ((0, 1), (0, -1), (-1, 0), (1, 0))
        for d in dirs:
            nr, nc = r+d[0], c+d[1]
            if self.isValid(nr, nc, grid) and grid[nr][nc] == '1':
                self.dfs(nr, nc, grid)

    def numIslands(self, grid):
        """

        :param grid: List[List[str]]
        :return: int
        """
        num_Islands = 0
        if not len(grid) or not len(grid[0]):
            return num_Islands
        rows, columns = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    self.dfs(r, c, grid)
                    num_Islands += 1
        return num_Islands