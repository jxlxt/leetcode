#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/23/18 7:21 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: 248.Strobogrammatic_NumberIII.py
# @Software: PyCharm


class Solution:
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        count, comb = 0, []
        for i in range(len(low), len(high) + 1):
            comb += (self.helper(i, i))
            print(comb)
        for num in comb:
            if ((len(num) == len(low) and int(num) - int(low) <
                    0) or (len(num) == len(high) and int(num) - int(high) > 0)):
                continue
            count += 1
        return count

    def helper(self, n, length):
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]

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
    sol = Solution()
    print(sol.strobogrammaticInRange(low='0', high='0'))
