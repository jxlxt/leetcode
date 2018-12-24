# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = collections.defaultdict(list)
        import queue
        queue = queue.Queue()
        queue.put((root, 0))
        while not queue.empty():
            node, x = queue.get()
            if node:
                results[x].append(node.val)
                queue.put((node.left, x - 1))
                queue.put((node.right, x + 1))
                
        return [results[i] for i in sorted(results)]

