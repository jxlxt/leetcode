#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/11/18 11:43 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: test.py
# @Software: PyCharm

class Node:
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        # when tree is empty
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left_child is None:
                cur_node.left_child = node
                return
            else:
                queue.append(cur_node.left_child)
            if cur_node.right_child is None:
                cur_node.right_child = node
                return
            else:
                queue.append(cur_node.right_child)

    def bfs(self):
        """
        breadth first search
        level order
        :return: List[int]
        """
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)
            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)

    def preorder(self, node):
        """
        root left right
        :return: List[int]
        """
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.left_child)
        self.preorder(node.right_child)

    def inorder(self, node):
        """
        left root right
        :return: List[int
        """
        if node is None:
            return
        self.inorder(node.left_child)
        print(node.item, end=" ")
        self.inorder(node.right_child)

    def postorder(self, node):
        """
        left right root
        :return: List[int]
        """
        if node is None:
            return
        self.postorder(node.left_child)
        self.postorder(node.right_child)
        print(node.item, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.bfs()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
    print(" ")