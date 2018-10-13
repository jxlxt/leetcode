#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:15 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: floodFill.py
# @Software: PyCharm


class Solution:
    def isValid(self, image, r, c):
        row, col = len(image), len(image[0])
        if 0 <= r < row and 0 <= c < col and image[r][c] == self.color:
            return True
        else:
            return False

    def dfs(self, image, r, c, newColor):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr in dirs:
            nr, nc = r+dr[0], c+dr[1]
            if self.isValid(image, nr, nc):
                image[nr][nc] = newColor
                self.dfs(image, nr, nc, newColor)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.color = image[sr][sc]
        if image[sr][sc] == newColor:
            return image
        else:
            self.dfs(image, sr, sc, newColor)
        image[sr][sc] = newColor
        return image