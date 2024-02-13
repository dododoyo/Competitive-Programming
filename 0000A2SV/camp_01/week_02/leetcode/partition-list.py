# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # break the linked list into two parts and merge them again 
        right_dummy,left_dummy = ListNode(0),ListNode(0)
        prev_node,next_node = right_dummy,left_dummy

        while head:
            if head.val < x:
                prev_node.next,prev_node = head,head
            else:
                next_node.next,next_node = head,head
            head = head.next
        next_node.next = None
        prev_node.next = left_dummy.next

        return right_dummy.next
        