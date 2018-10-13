#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/12/18 6:10 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: findDuplicateSubtrees.py
# @Software: PyCharm

import collections


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def trv(root):
            if not root: return "null"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct

        nodes = collections.defaultdict(list)
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]
