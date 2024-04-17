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
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode tail = dummy;
        
        
        
        while(tail != null){
            if(tail.next != null && tail.next.val == val){
                tail.next = tail.next.next;
            }else{
            tail = tail.next;
            }
        }
        
        return dummy.next;
    }
}