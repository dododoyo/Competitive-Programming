# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node: Optional[ListNode]) -> None:
        """ 
        Instead of removing the current node we make it 
        the next node and remove the next node"""

        # copy the value of the next node 
        node.val = node.next.val
        # point the next pointer to the one after it
        node.next = node.next.next

        