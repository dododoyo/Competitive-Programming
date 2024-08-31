# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: 
            return head

        dummy = next_head = ListNode(None)
        dummy.next = head
        previous = current = head

        while True:
            count = 0
            while current and count < k:
                count += 1
                current = current.next

            if count == k:
                head, tail = current, previous
                for _ in range(k):
                    tmp = tail.next
                    tail.next = head
                    head = tail
                    tail = tmp
                    
                next_head.next = head
                next_head = previous
                previous = current

            else:  
                return dummy.next