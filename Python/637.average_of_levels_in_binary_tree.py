# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        levels = defaultdict(list)
        queue = [(root, 1)]
        level = 0
        while queue:
            cur_node, level = queue.pop(0)
            levels[level].append(cur_node.val)
            if cur_node.left is not None:
                queue.append((cur_node.left, level+1))
            if cur_node.right is not None:
                queue.append((cur_node.right, level+1))
        return [sum(levels[i])/len(levels[i]) for i in range(1, level+1)]
