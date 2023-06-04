# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:return head
        even_start = even = head.next
        odd = head
        #no need to check for odd != None 
        #because it comes before even
        while even != None and even.next != None:#O(n)
            odd.next = odd.next.next;odd = odd.next #O(1)
            even.next = even.next.next;even = even.next#O(1)
        odd.next = even_start#O(1)
        return head