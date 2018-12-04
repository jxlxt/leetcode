# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.depth = {}
        maxDepth = self.dfs(root)
        for i in range(1, maxDepth + 1):
            ans.append(self.depth.get(i))
        return ans
    
    def dfs(self, node):
        if not node:
            return 0
        d = max(self.dfs(node.left), self.dfs(node.right)) + 1
        if d not in self.depth:
            self.depth[d] = []
        self.depth[d].append(node.val)
        return d
