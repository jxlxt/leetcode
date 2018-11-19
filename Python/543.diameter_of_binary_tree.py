# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.depth(root)
        return self.ans
        
    def depth(self, root):
        if not root: return -1
        left, right = self.depth(root.left) + 1, self.depth(root.right) + 1
        self.ans = max(self.ans, left+right)
        return max(left, right)
