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
        ListNode tail = head;
        while(tail!= null){
            if(count.contains(tail)){
                return true;
            }
            count.add(tail);
            tail = tail.next;
            
            
        }
        return false;
    }
}