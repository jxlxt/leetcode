#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:17 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: ValidWordAbbr.py
# @Software: PyCharm


class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = {}
        for word in dictionary:
            abbr = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
            self.d[abbr] = word if abbr not in self.d else '' if self.d[abbr] != word else self.d[abbr]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        return abbr not in self.d or self.d[abbr] == word

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
