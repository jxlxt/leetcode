# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = float('-inf')
    
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if root is None: return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        sums = left + right + root.val
        self.result = max(self.result, sums)
        return max(left, right, 0) + root.val
