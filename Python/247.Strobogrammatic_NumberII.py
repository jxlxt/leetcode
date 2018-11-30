#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/22/18 9:32 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: 247.Strobogrammatic_NumberII.py
# @Software: PyCharm


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)

    def helper(self, n, length):
        if n == 0: return [""]
        if n == 1: return ["0", "1", "8"]

        middles = self.helper(n - 2, length)
        res = []
        for middle in middles:
            if n != length:
                res.append('0' + middle + '0')
            res.append('1' + middle + '1')
            res.append('6' + middle + '9')
            res.append('9' + middle + '6')
            res.append('8' + middle + '8')
        return res


if __name__ == '__main__':
    # Print all Strobogrammatic
    # number for n = 3
    sol = Solution()
    print(sol.findStrobogrammatic(5))
