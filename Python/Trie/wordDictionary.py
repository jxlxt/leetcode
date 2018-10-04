#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:35 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: wordDictionary.py
# @Software: PyCharm


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[None] = None

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def find(word, node):
            if not word:
                return None in node
            c, word = word[0], word[1:]
            if c != '.':
                return c in node and find(word, node[c])
            return any(find(word, kid) for kid in node.values() if kid)
        return find(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)