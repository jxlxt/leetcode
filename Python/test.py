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
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        height = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        dp, length = [0] * len(height), 0

        import bisect
        for h in height:
            i = bisect.bisect_left(dp, h, 0, length)
            dp[i] = h
            if i == length:
                length += 1
        return length

class binheap:
    def __init__(self):
        self.heaplist = [0]
        self.countsize = 0


if __name__ == "__main__":
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    sol = Solution()
    print(sol.maxEnvelopes(envelopes))
    # print(li)
    # quick_sort(li, 0, len(li)-1)