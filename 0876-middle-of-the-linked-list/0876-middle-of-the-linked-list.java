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
    public ListNode middleNode(ListNode head) {
        ListNode tail = head;
        int count = 0;
        while(tail != null){
            count++;
            tail = tail.next;
        }   
        tail = head;
        for(int i=0; i<count/2; i++){
            tail = tail.next;
        }
        
        return tail;
    }
}