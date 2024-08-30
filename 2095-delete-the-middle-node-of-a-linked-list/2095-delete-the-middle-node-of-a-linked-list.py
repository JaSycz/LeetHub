# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None

        current = head
        
        list_length = 0
        while current is not None:
            list_length+= 1 
            current = current.next
        
        
        before, after = None, None
        middle_node = list_length//2
        current = head

        for i in range(0,middle_node +2):
            if middle_node - 1 == i:
                before = current
            elif middle_node + 1 == i:
                after = current
            if current is not None:
                current = current.next
            
            


        before.next = after

        return head