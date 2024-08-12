# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, lis1: Optional[ListNode], lis2: Optional[ListNode]) -> Optional[ListNode]:
        if lis1 == None:
            return lis2
        elif lis2 == None:
            return lis1
        else:
            if lis1.val < lis2.val:
                lis1.next = self.mergeTwoLists(lis1.next, lis2)
                return lis1
            else:
                lis2.next = self.mergeTwoLists(lis1, lis2.next)
                return lis2