# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        left, right, sol = None, head, head.next
        while right and right.next:
            fut = right.next
            if left: left.next = fut
                
            right.next = fut.next
            fut.next = right
            
            left = right
            right = right.next

        return sol or head
        