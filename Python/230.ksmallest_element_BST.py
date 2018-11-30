# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
#         self.k = k
#         self.res = 0
#         self.helper(root)
#         return self.res
    
#     def helper(self, root):
#         # corner case
#         if not root:
#             return 0
#         self.helper(root.left)
#         self.k -= 1
#         if self.k == 0:
#             self.res = root.val
#             return
#         self.helper(root.right)
        stack = [root]
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
