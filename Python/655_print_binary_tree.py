# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # get the height of tree
        h = self.getHeight(root)
        # widrh = 2 ^ height - 1
        w = (1 << h) - 1 
        # initialize the result
        res = [["" for _ in range(w)] for _ in range(h)]
        self.fillMatrix(root, res, 0, 0, w-1)
        return res
    
    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
    
    def fillMatrix(self, root, res, height, left, right):
        if not root:
            return 
        mid = (left + right) // 2
        res[height][mid] = str(root.val)
        self.fillMatrix(root.left, res, height + 1, left, mid - 1)
        self.fillMatrix(root.right, res, height + 1, mid + 1, right)
