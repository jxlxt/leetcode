# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs solution
        # corner case
        if not root: return 0
        # stack, res = [(root, root.val)], 0   
        # while stack:
        #     node, val = stack.pop()
        #     if node:
        #         if not node.left and not node.right:
        #             res += val
        #         if node.left:
        #             stack.append((node.left, val*10 + node.left.val))
        #         if node.right:
        #             stack.append((node.right, val*10 + node.right.val))
        # return res
    
        # bfs solution
        # queue, res = collections.deque([(root, root.val)]), 0
        # while queue:
        #     node, val = queue.popleft()
        #     if node:
        #         if not node.left and not node.right:
        #             res += val
        #         if node.left:
        #             queue.append((node.left, val*10 + node.left.val))
        #         if node.right:
        #             queue.append((node.right, val*10 + node.right.val))
        # return res
        
        # recursively
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, value):
        if root:
            self.dfs(root.left, value*10 + root.val)
            self.dfs(root.right, value*10 + root.val)
            if not root.right and not root.left:
                self.res += value*10 + root.val
