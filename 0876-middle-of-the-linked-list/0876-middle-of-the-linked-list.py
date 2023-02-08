# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #lets use two pointers one moving twice as fast as the first
        #aks Hare and Tortoise algorithm
         
        fastPointer = head
        slowPointer = head
        
        while(fastPointer!= None and fastPointer.next != None):
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            
        return slowPointer