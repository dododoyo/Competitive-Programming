# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node):
        prev = None 
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        return prev
    def add(self,ll1,ll2):
        carry = 0
        prev = ListNode(-1)
        dummy = prev

        while ll1 or ll2 or carry:
            summ = carry
            if ll1:
                summ += ll1.val
                ll1 = ll1.next
            if ll2:
                summ += ll2.val
                ll2 = ll2.next

            # calculate 
            curr_node = ListNode(summ%10)
            carry = summ//10

            # update pointers
            prev.next = curr_node
            prev = curr_node

        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse both lists 
        rl1 = self.reverse(l1)
        rl2 = self.reverse(l2)

        # add the from the back  
        rsolution = self.add(rl1,rl2)
        solution = self.reverse(rsolution)

        return solution