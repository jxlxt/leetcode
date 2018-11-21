# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = self.findMid(head)
        l2 = self.reverseList(mid.next)
        mid.next = None
        l1 = head
        self.mergeList(l1, l2)
    # split the list into two part, the fisrt list >= the second half list
    def findMid(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    # Reverses in place a list.
    def reverseList(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
    # merge two lists
    def mergeList(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            cur.next = l1
            cur = l1
            l1 = l1.next
            
            cur.next = l2
            cur = l2
            l2 = l2.next
            
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
