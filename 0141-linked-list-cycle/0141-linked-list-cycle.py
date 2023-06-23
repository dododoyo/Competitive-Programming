# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:return False#for zero nodes
        if head.next == None:return False#for only one node
        if head == head.next:return True#for only two nodes

        slow = head;fast = head.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:return True
        return False
        