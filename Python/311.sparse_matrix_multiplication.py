#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/26/18 11:05 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: 311.sparse_matrix_multiplication.py
# @Software: PyCharm
from collections import defaultdict


class Solution:
    # solution 1: ignore the 0 element in matrix A and B
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        mapAI = defaultdict(list)  # map j to a list of i, where A[i][j] != 0
        mapBK = defaultdict(list)  # map j to a list of k, where B[j][k] != 0

        for i, Row in enumerate(A):
            for j, n in enumerate(Row):
                if n != 0:
                    mapAI[j].append(i)

        for j, Row in enumerate(B):
            for k, n in enumerate(Row):
                if n != 0:
                    mapBK[j].append(k)

        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

        for j in range(len(B)):
            for i in mapAI[j]:
                for k in mapBK[j]:
                    res[i][k] += A[i][j] * B[j][k]

        return res

    # solution 2: store the column which has element
    def multiply_2(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, k = len(A), len(A[0]), len(B[0])
        res = [[0] * k for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for t in range(k):
                        if B[j][t] != 0:
                            res[i][t] += A[i][j] * B[j][t]
        return res

