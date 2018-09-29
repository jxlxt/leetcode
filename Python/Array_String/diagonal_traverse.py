#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

"""
      Explaination:
      1. Assume in each pair i, bi >= ai.
      2. Denote Sm = min(a1, b1) + min(a2, b2) + ... + min(an, bn). The biggest Sm is the answer of this problem. Given 1, Sm = a1 + a2 + ... + an.
      3. Denote Sa = a1 + b1 + a2 + b2 + ... + an + bn. Sa is constant for a given input.
      4. Denote di = |ai - bi|. Given 1, di = bi - ai. Denote Sd = d1 + d2 + ... + dn.
      5. So Sa = a1 + a1 + d1 + a2 + a2 + d2 + ... + an + an + dn = 2Sm + Sd => Sm = (Sa - Sd) / 2. To get the max Sm, given Sa is constant, we need to make Sd as small as possible.
      6. So this problem becomes finding pairs in an array that makes sum of di (distance between ai and bi) as small as possible. Apparently, sum of these distances of adjacent elements is the smallest. If that's not intuitive enough, see attached picture. Case 1 has the smallest Sd.
"""

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Time complexity: O(M*N) M is the width of the matrix and N is the
        # height of the matrix
        # Space complexity: O(1)
        """
        Move to the upper right When the upper boundary is encountered, if it does not reach the right boundary, move to the right (offset: row +0, column +1), otherwise move downward (offset: row +1, column +0) )

When moving to the lower left encounters the left boundary, if it does not reach the lower boundary, it moves down (offset: row +1, column +0), otherwise it moves to the right (offset: row +0, column +1) )
        """
        if not matrix: return []
        # start point
        i, j, k, ans = 0, 0, 1, []
        w, h, res = len(matrix), len(matrix[0]), []
        for _ in range(w*h):
            res.append(matrix[i][j])
            if k > 0:
                # offset to move upper right corner
                di, dj = i - 1, j + 1
            else:
                # offset to move bottom left corner
                di, dj = i + 1, j - 1
            if 0 <= di < w and 0 <= dj < h:
                i, j = di, dj
            else:
                # check for the corner
                if k > 0:
                    if j + 1 < h:
                        j += 1
                    else:
                        i += 1
                else:
                    if i + 1 < w:
                        i += 1
                    else:
                        j += 1
                k *= -1
        return ans
