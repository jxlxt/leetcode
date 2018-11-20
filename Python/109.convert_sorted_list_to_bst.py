# official solution: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.cur = None
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.cur = head
        n = self.getSize(head)
        return self.myTree(n)
    
    def myTree(self, n):
        if n <= 0:
            return None
        left = self.myTree(n // 2)
        root = TreeNode(self.cur.val)
        self.cur = self.cur.next
        right = self.myTree(n - n // 2 - 1)
        root.left, root.right = left, right
        return root
        
    def getSize(self, head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n
