# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #let's use two pointers
        #one pointed at the head at first
        #another pointed +k from the first
        
        firstPointer = head
        secondPointer = head
    
        
        for i in range(n):
            firstPointer = firstPointer.next
            
            
        if not firstPointer:
            return head.next
            
        while(firstPointer.next):
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
            
        #secondPointer.val = secondPointer.next.val
        secondPointer.next = secondPointer.next.next
        
        
        return head
