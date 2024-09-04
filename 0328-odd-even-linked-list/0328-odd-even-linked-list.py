# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        tmp = head
        end = head
        count = 0
        while end.next is not None:
            end = end.next
            count+=1

        if (count % 2 == 0):
            count = count//2
        else:
            count = count//2 +1
        while(count>0):
            end.next = tmp.next
            tmp.next = tmp.next.next
            end.next.next = None

            end = end.next
            tmp = tmp.next

            count-= 1

        return head
