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
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0 or len(num2) == 0:
            return "0"
        digits, product, sum_ = [0] * (len(num2) + len(num1)), 0, 0
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                p1, p2 = i + j, i + j + 1
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = product + digits[p2]
                digits[p1] += sum_ // 10
                digits[p2] = sum_ % 10
        res = []
        for digit in digits:
            if not (len(res) == 0 and digit == 0):
                res.append(digit)
        return ''.join(map(str, res))


if __name__ == "__main__":
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(li)
    # quick_sort(li, 0, len(li)-1)
    sol = Solution()
    num1 = "2"
    num2 = "3"
    print(sol.multiply(num1, num2))