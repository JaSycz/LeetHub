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
        HashSet<ListNode> count = new HashSet<>();
        while(head!= null){
            if(count.contains(head)){
                return true;
            }
            count.add(head);
            head = head.next;
            
            
        }
        return false;
    }
}