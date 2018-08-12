# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        # first method: recursive
        a = root.val
        kid = root.left if target < a else root.right
        if not kid: return a
        b = self.closestValue(kid, target)
        return min((b,a), key = lambda x: abs(target -x))

        # second method: iterative
        path = []
        while root:
            path += root.val,
            root = root.left if target < root.val else root.right
        return min(path[::-1], key = lambda x: abs(target-x))
        # [::-1] negative values also work to make a copy of the same list in
        # reverse order
