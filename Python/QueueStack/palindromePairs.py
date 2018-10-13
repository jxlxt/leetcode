#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:53 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: palindromePairs.py
# @Software: PyCharm


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palidrome(check):
            return check == check[::-1]

        words = {words:i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palidrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], k])
                if j!= n and is_palidrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals
