# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # if not root:
        #     return []
        # res, stack = [], [(root, "")]
        # while stack:
        #     node, ls = stack.pop()
        #     if not node.left and not node.right:
        #         res.append(ls + str(node.val))
        #     if node.left:
        #         stack.append((node.left, ls+str(node.val)+"->"))
        #     if node.right:
        #         stack.append((node.right, ls+str(node.val)+"->"))
        # return res
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return [str(root.val) + "->" + i for i in
        self.binaryTreePaths(root.left)] + [str(root.val) + "->" + j for j in
        self.binaryTreePaths(root.right)]
