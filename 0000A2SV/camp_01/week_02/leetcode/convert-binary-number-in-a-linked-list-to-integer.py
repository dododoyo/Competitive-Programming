# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        digits = 0
        count_head = head
        while count_head:
            count_head = count_head.next
            digits += 1
        solution = 0
        while head:
            solution += head.val*(2**(digits-1))
            digits -= 1
            head = head.next
        return solution
        
        