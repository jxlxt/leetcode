#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/2/18 9:07 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: cloneGraph.py
# @Software: PyCharm

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighborsl.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])