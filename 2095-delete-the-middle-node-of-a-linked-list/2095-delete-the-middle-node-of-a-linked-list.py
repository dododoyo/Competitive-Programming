# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if the linkedlist has only one node remove it 
        if head.next == None:return None
        
        slow_pointer = head
        fast_pointer = head.next.next
        
        
        while fast_pointer != None and fast_pointer.next != None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        
        slow_pointer.next = slow_pointer.next.next
        return head