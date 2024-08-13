# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left,right = head,head.next
        prev_left = head
        current_sum = 0

        while right:
            if right.val != 0:
                current_sum += right.val
            else:
                left.val = current_sum
                prev_left = left # used to cutoff the linkedlist later
                left = left.next
                current_sum = 0
            
            right = right.next
        
        prev_left.next = None # remove last left

        # Time = O(nodes in linkedlist)
        # Space = O(1)

        return head


        