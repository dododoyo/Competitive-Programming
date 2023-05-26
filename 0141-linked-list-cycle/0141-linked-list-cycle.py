# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checker = set()
        while head != None:
            if head in checker:return True
            else:checker.add(head);head=head.next
        return False
        