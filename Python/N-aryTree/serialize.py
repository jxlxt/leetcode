#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/8/18 9:59 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: serialize.py
# @Software: PyCharm

from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        serial = []

        def preorder(node):

            if not root:
                return

            serial.append(str(node.val))
            for child in node.children:
                preorder(child)

            serial.append("#")

        preorder(root)
        return " ".join(serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def helper(node):

            if not tokens:
                return

            while tokens[0] != "#":
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)

            tokens.popleft()

        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
