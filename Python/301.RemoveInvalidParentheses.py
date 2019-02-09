#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2/4/19 11:07 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: 301.RemoveInvalidParentheses.py
# @Software: PyCharm
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else left
        ans = []
        self.dfs(s, 0, left, right, ans)
        return ans

    def dfs(self, s, start, l, r, ans):
        if l == 0 and r == 0:
            if self.isValid(s):
                if s in ans: return
                ans.append(s)
                return
        for i in range(start, len(s)):
            # avoid duplication
            if i != start and s[i] == s[i - 1]: continue
            if s[i] == '(' or s[i] == ')':
                curr = s
                curr = s[:i] + s[i + 1:]
                if r > 0:
                    self.dfs(curr, i, l, r - 1, ans)
                elif l > 0:
                    self.dfs(curr, i, l - 1, r, ans)

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(': count += 1
            if c == ')': count -= 1
            if count < 0: return False
        return count == 0


if __name__ == '__main__':
    sol = Solution()
    s = ")k)))())()())))())"
    print(sol.removeInvalidParentheses(s))
