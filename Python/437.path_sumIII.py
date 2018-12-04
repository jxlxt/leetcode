# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.cache = {0: 1}
        self.res = 0
        
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # self.dfs(root, sum)
        self.dfs_memo(root, target, 0, self.cache)
        return self.res
        
    # slution 1: basic dfs search  
    def dfs(self, node, target):
        if node is None:
            return
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
    
    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.res += 1
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)
        
    # solution 2: memorization of path sum
    def dfs_memo(self, node, target, current_path, cache):
        if node is None:
            return
        current_path += node.val
        oldpath_sum = current_path - target
        self.res += cache.get(oldpath_sum, 0)
        cache[current_path] = cache.get(current_path, 0) + 1
        
        self.dfs_memo(node.left, target, current_path, cache)
        self.dfs_memo(node.right, target, current_path, cache)
        
        cache[current_path] -= 1
