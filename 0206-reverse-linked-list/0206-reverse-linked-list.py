# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #let's manipulate the pointers in place to get a reversed linked list
        
        if(head == None):
            return None
        
        if(head.next == None):
            return head

        #make next node to previous
        
        currentNode = head
        previousNode = None
        
        while (currentNode != None):
            nextNode = currentNode.next
            
            #make current node's pointer to its next node
            currentNode.next = previousNode
            
            #next node's previous node will be current node
            previousNode = currentNode
            
            #the next current node is the next node
            currentNode = nextNode
            
        #at the end of the iteration previous node will be the last node
        #because current node pointer will be at end(None)
        #so make head of the pointer to the last node
        
        head = previousNode
        
        return head
            
            
            
        