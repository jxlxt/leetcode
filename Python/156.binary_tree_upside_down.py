# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        return self.dfs(root)
        
    def dfs(self, cur):
        if not cur.left: 
            return cur
        newRoot = TreeNode(cur.left)
        newRoot = self.dfs(cur.left)
        cur.left.right = cur
        cur.left.left = cur.right
        cur.left = None
        cur.right = None
        return newRoot
        
