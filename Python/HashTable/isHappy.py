#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 5:54 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: isHappy.py
# @Software: PyCharm


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isHappy(19))
