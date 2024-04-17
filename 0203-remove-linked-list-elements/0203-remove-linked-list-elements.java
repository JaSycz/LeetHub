/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode tail = head;
        
        while(tail != null){
            if(tail.next != null && tail.next.val == val){
                tail.next = tail.next.next;
            }else{
            tail = tail.next;
            }
        }
        if(head != null && head.val == val){
            head = head.next;
        }
        return head;
    }
}