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
    public boolean isPalindrome(ListNode head) {
        ListNode fastptr = head;
        ListNode slowptr = head;
        while(fastptr!=null && fastptr.next!=null){
            slowptr = slowptr.next;
            fastptr = fastptr.next.next;
        }
       ListNode tmp=null;
       ListNode reverseMiddle=null;
       ListNode middle = slowptr;
       while(middle!=null){
            tmp = middle.next;
            middle.next = reverseMiddle;
            reverseMiddle = middle;
            middle = tmp;
       }
       while(reverseMiddle!=null){
        if(reverseMiddle.val != head.val){
            return false;
        }
        reverseMiddle = reverseMiddle.next;
        head = head.next;
       } 
        
        return true;
    }
}