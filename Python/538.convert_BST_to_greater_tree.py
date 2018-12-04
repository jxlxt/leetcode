# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.helper(root)
        return root
        
    def helper(self, node):
        if not node:
            return 
        if node.right:
            self.helper(node.right)
        self.sum += node.val
        node.val = self.sum
        if node.left:
            self.helper(node.left)
