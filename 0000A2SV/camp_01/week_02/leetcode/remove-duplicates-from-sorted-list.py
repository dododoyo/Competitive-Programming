# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        left,right = head,head.next
        while right:
            if left.val == right.val:
                # remove right 
                left.next = right.next
                right = left.next
            else:
                right,left = right.next,left.next
        return head