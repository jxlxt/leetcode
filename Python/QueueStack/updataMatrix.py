#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:20 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: updataMatrix.py
# @Software: PyCharm


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        q, m, n = [], len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 0x7fffffff
                else:
                    q.append((i, j))
        for i, j in q:
            for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
                z = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                    matrix[r][c] = z
                    q.append((r, c))
        return matrix