# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        odd_nodes =  ListNode(val=head.val)
        even_nodes = ListNode(val=head.next.val)
        current = head.next.next
        count = 3
        odd_tail,even_tail = odd_nodes,even_nodes

        while current is not None:
            if count % 2  == 0:
                 even_tail.next = ListNode(val=current.val)
                 even_tail = even_tail.next
            else:
                odd_tail.next = ListNode(val=current.val)
                odd_tail = odd_tail.next
                 
            current = current.next
            count+=1
        odd_tail.next = even_nodes
        
        return odd_nodes
