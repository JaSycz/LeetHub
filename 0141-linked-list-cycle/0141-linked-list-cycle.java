/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode  firstPoint = head;
        ListNode  secondPoint = head;
        while(secondPoint != null && secondPoint.next!= null){
            firstPoint = firstPoint.next;
            secondPoint = secondPoint.next.next;
                
            if(firstPoint == secondPoint){
                return true;
            }
            
        }
        return false;
    }
}