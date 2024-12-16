# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)


        start_node = dummy
        # break the window to be reversed 
            # get start node 
        for _ in range(left-1):
            start_node = start_node.next
        end_node = start_node

            # get ending node and register it
        for _ in range(right-left+1):
            end_node = end_node.next

        second_part = end_node.next

            # make ending node point to None 
        end_node.next = None 

        # reverse the window 
        reversed_head,reversed_tail = self.reverseList(start_node.next)
        x = reversed_head
        while x:
            print(x.val)
            x = x.next

        # append it to the original linked lis
            # make start node next to new reversed head 
        start_node.next = reversed_head
        reversed_tail.next = second_part

        return dummy.next

            # make ending ndoe of reversed to second part of ll
    def reverseList(self,node):
        # given the head of the linkedlist to be reversed
        # use iteration to reverse the window 
        # return head and tail of the window
        if not node.next:
            return node , node

        tail = node # after reversing prev head is going to be the new tail 
        prev = None 
        while node:
            next_node = node.next

            node.next = prev 

            prev = node
            node = next_node
        
        return prev,tail

        
