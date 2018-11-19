class Solution:
    def reverseBetween(self, head, start, end):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy_head = sublist_head = ListNode(0)
        sublist_head.next = head
        for _ in range(1, start):
            sublist_head = sublist_head.next
        
        # reverses sublist
        sublist_iter = sublist_head.next
        for _ in range(end - start):
            temp = sublist_iter.next
            sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                               sublist_head.next,
                                                                temp)
        return dummy_head.next    
