#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/17/18 4:28 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: test.py
# @Software: PyCharm




# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         size, res = len(s) + 1, ""
#         for i in range(size):
#             for j in range(size):
#                 t = s[i:j]
#                 if self.isPalindromic(t):
#                     if len(t) > len(res):
#                         res = t
#                 else:
#                     continue
#         return res
#
#     def isPalindromic(self, t):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         return t == t[::-1]
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.longestPalindrome(s))

def quick_sort(alist, first, last):
    if first >= last:
        return

    n = len(alist)
    low, mid_value, high = first, alist[first], last

    while low < high:
        while low < high and alist[low] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[high] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick_sort(alist, first, low -1)
    quick_sort(alist, low+1, last)


class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1, l2 = len(s1), len(s2)
        # initailzation
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, l2+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]))
        return dp[l1][l2]


class binheap:
    def __init__(self):
        self.heaplist = [0]
        self.countsize = 0


if __name__ == "__main__":
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    s1 = "sea"
    s2 = "eat"
    sol = Solution()
    print(sol.minimumDeleteSum(s1, s2))
    # print(li)
    # quick_sort(li, 0, len(li)-1)