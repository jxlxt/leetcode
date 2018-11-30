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


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True




if __name__ == "__main__":
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(li)
    # quick_sort(li, 0, len(li)-1)
    sol = Solution()
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    left, right = 0, len(s) - 1
    print(s[left:right])
    print(s[left+1:right+1])