# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
            
        odd_node = head
        first_even = even_node = head.next

        while even_node and even_node.next:
            # for each odd number we point it to the next odd number
            odd_node.next = odd_node.next.next
            odd_node = odd_node.next
            # for each even number we point it to the next even number
            even_node.next = even_node.next.next
            even_node = even_node.next

        # connect the tail of odd the first even
        odd_node.next = first_even
        return head

        
        