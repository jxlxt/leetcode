#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:07 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: groupStrings.py
# @Software: PyCharm


class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for i in strings:
            hs = self.strHash(i)
            if hs not in dictionary.keys():
                dictionary[hs] = [str(i)]
            else:
                self.insertStr(dictionary[hs], str(i))
        return [dictionary[key] for key in dictionary.keys()]

    def strHash(self, astring):
        hslist = [(ord(i) - ord(astring[0])) % 26 for i in astring]
        return tuple(hslist)

    def insertStr(self, alist, astring):
        i = 0
        while i < len(alist) and ord(astring[0]) > ord(alist[i][0]):
            i += 1
        if i == len(alist):
            alist.append(astring)
        else:
            alist[:] = alist[0:i] + [astring] + alist[i:]
