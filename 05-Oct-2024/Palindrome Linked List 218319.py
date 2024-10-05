# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        prev_slow,slow= None,head
        fast= head
        while fast and fast.next:
            # move the pointers
            # with different speeds
            fast = fast.next.next
            next_slow = slow.next
            # reverse the linkedlist
            # before the slow pointer
            slow.next = prev_slow
            prev_slow = slow
            slow = next_slow
            
        left,right = prev_slow,slow

        # checking if length is odd
        if fast:right = slow.next
        # print(right)
        # print(left.val,right.val)

        while right and left:
            if right.val != left.val:
                return False
            right,left = right.next,left.next
        return True
            
