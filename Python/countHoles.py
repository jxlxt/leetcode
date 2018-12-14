#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/13/18 1:33 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: countHoles.py
# @Software: PyCharm
import math


def factorization(nums):
    res = []
    dfs(res, [], nums, 2)
    return res


def dfs(result, path, num, factor):
    if num <= 1:
        if len(path) > 1:
            result.append(path[:])
        return

    for i in range(factor, int(math.sqrt(num))+1):
        if num % i == 0:
            path.append(i)
            dfs(result, path, num // i, i)
            path.pop()

    if num >= factor:
        path.append(num)
        dfs(result, path, 1, num)
        path.pop()


class Solution:
    # @param {int} n an integer
    # @return {int[][]} a list of combination
    def getFactors(self, n):
        # write your code here
        result = []
        self.helper(result, [], n, 2);
        return result

    def helper(self, result, item, n, start):
        if n <= 1:
            if len(item) > 1:
                result.append(item[:])
            return

        import math
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                item.append(i)
                self.helper(result, item, n // i, i)
                item.pop()

        if n >= start:
            item.append(n)
            self.helper(result, item, 1, n)
            item.pop()


nums = 12
sol = Solution()
# print(sol.getFactors(nums))
print(factorization(nums))
