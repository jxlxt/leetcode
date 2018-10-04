#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 9:03 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: evalRPN.py
# @Software: PyCharm


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l+r)
                elif t == '-':
                    stack.append(l-r)
                elif t == '*':
                    stack.append(l*r)
                else:
                    if l*r < 0 and l%r != 0:
                        stack.append(l//r+1)
                    else:
                        stack.append(l//r)
        return stack.pop()