#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:48 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: wordSquares.py
# @Software: PyCharm


import collections


class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n = len(words[0])
        fulls = collections.defaultdict(list)
        for word in words:
            for i in range(n):
                fulls[words[:i]].append(word)

        def build(square):
            if len(square) == n:
                squares.append(square)
                return
            for word in fulls[''.join(zip(*square)[len(square)])]:
                build(square + [word])
        squares = []
        for word in words:
            build([word])
        return squares
