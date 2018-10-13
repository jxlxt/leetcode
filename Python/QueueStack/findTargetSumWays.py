#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 9:10 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: findTargetSumWays.py
# @Software: PyCharm


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        '''
        DP solution
        '''
    #     dp = collections.Counter()
    #     dp[0] = 1
    #     for n in nums:
    #         ndp = collections.Counter()
    #         for sgn in (-1, 1):
    #             for k in dp.keys():
    #                 ndp[k+n*sgn] += dp[k]
    #         dp = ndp
    #     return dp[S]
        '''
        DFS solution
        '''
        cache = {}

        def findTarget(i, s):
            if (i, s) not in cache:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = findTarget(i+1, s-nums[i])+findTarget(i+1, s+nums[i])
                cache[(i, s)] = r
            return cache[(i, s)]
        return findTarget(0, S)