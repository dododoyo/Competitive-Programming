# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:return head
        even_nodes =first_even= head.next
        odd_nodes = head
        
        while even_nodes != None and even_nodes.next != None:
            odd_nodes.next = odd_nodes.next.next;odd_nodes=odd_nodes.next;
            even_nodes.next = even_nodes.next.next;even_nodes=even_nodes.next;
        odd_nodes.next = first_even
        return head