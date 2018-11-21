# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # dfs solution
#         res = []
#         self.dfs(root, 0, res)
#         return res
            
#     def dfs(self, root, level, res):
#         if not root:
#             return
#         # add the first node of each level to res
#         if level == len(res):
#             res.append(root.val)
#         self.dfs(root.right, level+1, res)
#         self.dfs(root.left, level+1, res)

        # BFS + queue
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return [x[-1] for x in res]
