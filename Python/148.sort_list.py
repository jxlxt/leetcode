# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # divide and conquer
        # merge sort
        # O(nlogN) time complexity
        # constant space complexity
        if not head or not head.next: return head
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        left, right = self.sortList(head), self.sortList(slow)
        return self.mergeList(left, right)
        
    def mergeList(self, left, right):
        if not left or not right: return left or right
        dummy = prev = ListNode(0)
        while left and right:
            if left.val < right.val:
                prev.next, left = left, left.next
            else:
                prev.next, right = right, right.next
            prev = prev.next
        prev.next = left if left else right
        return dummy.next
        
