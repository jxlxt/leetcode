package edu.ucsc;

public class removeElements {
    public ListNode removeElements(ListNode head, int val) {
        ListNode cur = head;
        ListNode fakeHead = new ListNode(-1);
        fakeHead.next = head;
        ListNode prev = fakeHead;
        while (cur != null) {
            if (cur.val == val) {
                prev.next = cur.next;
            }else {
                prev = prev.next;
            }
            cur = cur.next;
        }
        return fakeHead.next;
    }
}
