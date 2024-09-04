# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        stack = []
        count = 0
        start = head
        end,mid = head, head

        while end is not None:
            mid = mid.next
            end = end.next.next
        mid2 = mid
        while mid is not None:
            stack.append(mid.val)
            mid = mid.next
        max = 0
        while start is  not mid2:
            local_max = start.val + stack.pop()
            if ( local_max > max):
                max = local_max
            start = start.next

        return max



        