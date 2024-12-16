# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        while head:
            next_node = head.next
            head.next = prev
            
            prev = head
            head = next_node
        # new head is prev 
        new_head = prev
        return new_head