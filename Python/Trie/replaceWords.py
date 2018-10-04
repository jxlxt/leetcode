#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:32 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: replaceWords.py
# @Software: PyCharm

import collections


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentenceList = sentence.split(" ")
        for i in range(len(sentenceList)):
            for j in dict:
                if sentenceList[i].startswith(j):
                    sentenceList[i] = j
        return " ".join(sentenceList)

        # Trie method
        # _trie = lambda: collections.defaultdict(_trie)
        # trie = _trie()
        # END = True
        # for root in roots:
        #     cur = trie
        #     for letter in root:
        #         cur = cur[letter]
        #     cur[END] = root
        #
        # def replace(word):
        #     cur = trie
        #     for letter in word:
        #         if letter not in cur: break
        #         cur = cur[letter]
        #         if END in cur:
        #             return cur[END]
        #     return word
        #
        # return " ".join(map(replace, sentence.split()))