#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:12 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: decodeString.py
# @Software: PyCharm


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # in the string, there are four situations, num, '[', ']' and char
        # for num, we should store the repeat time of the charters in []
        # at the start of '[' we begin store the characters
        # and at the end of ']', we calculate the result with num*char
        # the store the result into the final ans
        stack = []
        stack.append(["", 1])
        num = ""
        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                stack.append(["", int(num)])
            elif char == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += char
        return stack[0][0]