# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find cycle starting from the head move meeting 
        # heads and head equally where they meet is cycle entrance
        slow,fast = head,head
        while fast and fast.next:
            slow ,fast= slow.next ,fast.next.next
            if slow == fast:
                break
        else:
            # if not (fast and fast.next) we have reached the end
            return None

        # move two pointers equally to get to the cycle entrance
        while head:
            if head == slow:
                return slow
            head, slow = head.next, slow.next