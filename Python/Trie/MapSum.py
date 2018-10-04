#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/3/18 8:28 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: MapSum.py
# @Software: PyCharm

class TrieNode():
    """
    implement a Trie data structure
    """
    def __init__(self, count = 0):
        self.count = count
        self.children = {}


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        p = self.trie
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val
        for c in key:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
            p.count += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        p = self.trie
        for char in prefix:
            if char not in p.children:
                return 0
            p = p.children[char]
        return p.count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)