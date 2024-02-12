# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left,right = head,head
        while n > 0:
            right = right.next
            n -= 1
        if right == None:
            return head.next

        while right and right.next:
            right,left = right.next,left.next
            
        if left.next:left.next = left.next.next
        else:left.next = None
        return head
        