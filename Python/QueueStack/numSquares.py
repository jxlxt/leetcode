#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 10:14 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: numSquares.py
# @Software: PyCharm


class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        BFS solution
        '''
    #     if n < 2:
    #         return n
    #     i, lst = 1, []
    #     while i*i <= n:
    #         lst.append(i*i)
    #         i += 1
    #     cnt, toCheck = 0, {n}
    #     while toCheck:
    #         cnt += 1
    #         tmp = set()
    #         for x in toCheck:
    #             for y in lst:
    #                 if x == y: return cnt
    #                 if x < y: break
    #                 tmp.add(x-y)
    #         toCheck = tmp
    #     return cnt
        '''
        Mathmatic Solution
        '''
        # sqrt_n = sqrt(n)
        # if sqrt_n == int(sqrt_n):
        #     return 1
        #
        # for i in range(1, int(sqrt_n)):
        #     tmp = sqrt(n-i*i)
        #     if int(tmp) == tmp:
        #         return 2
        #
        # m = n
        # while m%4 == 0:
        #     m >>= 2
        # if m%8 != 7:
        #     return 3
        #
        # return 4
        '''
        DP solution
        '''
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]