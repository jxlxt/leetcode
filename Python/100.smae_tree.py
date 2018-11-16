# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return p == q
        # DFS solution
        # stack = [(p, q)]
        # while stack:
        #     node_1, node_2 = stack.pop()
        #     if not node_1 and not node_2:
        #         continue
        #     elif None in [node_1, node_2]:
        #         return False
        #     else:
        #         if node_1.val != node_2.val:
        #             return False
        #         else:
        #             stack.append((node_1.left, node_2.left))
        #             stack.append((node_1.right, node_2.right))
        # return True
        
        # BFS solution
        queue = [(p, q)]
        while queue:
            node_1, node_2 = queue.pop(0)
            if not node_1 and not node_2:
                continue
            elif None in [node_1, node_2]:
                return False
            else:
                if node_1.val != node_2.val:
                    return False
                else:
                    queue.append((node_1.left, node_2.left))
                    queue.append((node_1.right, node_2.right))
        return True
