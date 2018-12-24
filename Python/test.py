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


def almost_palindromes(str):
    length = len(str)
    a, b = 0, length - 1
    total = 0

    while (a < length):
        if (str[a] != str[b]):
            total += 1
        a += 1
        b -= 1

    return total


def printRect(X, Y, n):
    # find Xmax and Xmin
    Xmax = max(X)
    Xmin = min(X)

    # find Ymax and Ymin
    Ymax = max(Y)
    Ymin = min(Y)

    # print all four coordinates
    print("{", Xmin, ", ", Ymin, "}", sep="")
    print("{", Xmin, ", ", Ymax, "}", sep="")
    print("{", Xmax, ", ", Ymax, "}", sep="")
    print("{", Xmax, ", ", Ymin, "}", sep="")



# driver program
X = [4, 3, 6, 1, -1, 12]
Y = [4, 1, 10, 3, 7, -1]
n = len(X)
printRect(X, Y, n)
# This code is contributed by
# Smitha Dinesh Semwal