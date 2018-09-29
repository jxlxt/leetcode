#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:56 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: implement_trie.py
# @Software: PyCharm

import collections

class TrieNode():

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize the data structure
        """
        self.trie = TrieNode()

    def insert(self, word):
        p = self.trie
        for c in word:
            p = p.children[c]
        p.is_word = True

    def search(self, word):
        p = self.trie
        for c in word:
            p = p.children.get(c)
            if p is None:
                return False
        return p.is_word

    def startWith(self, prefix):
        p = self.trie
        for c in prefix:
            p = p.children.get(c)
            if p is None:
                return False
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    param_2 = obj.search('app')
    param_3 = obj.startWith('app')
    print(param_2)
    print(param_3)
