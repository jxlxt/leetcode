# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        # top down dfs
        return self.dfs(root, None, 0)
    
    def dfs(self, node: TreeNode, parent: TreeNode, ans: int) -> int:
        if not node:
            return ans
        if parent and node.val == parent.val + 1:
            ans += 1
        else:
            ans = 1
        return max(ans, max(self.dfs(node.left, node, ans), self.dfs(node.right, node, ans)))
