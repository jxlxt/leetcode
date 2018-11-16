i# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = head.next
        prev = ListNode(0)
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head
            prev.next = temp
            head = head.next
            prev = temp.next
        return dummy
