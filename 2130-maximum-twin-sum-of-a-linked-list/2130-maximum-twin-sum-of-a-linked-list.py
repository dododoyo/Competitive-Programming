# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast,slow = head,head
        prev = None
        while fast and fast.next:
            #move the fast pointer by two values
            fast = fast.next.next
            #store where the next pointer of slow is pointing
            tmp = slow.next
            #point slow to previous
            slow.next = prev
            #register current slow as next iterations previous
            prev = slow
            #point the next slow
            slow = tmp
        solution = 0
        while slow != None and prev != None:
            solution = max(solution,prev.val+slow.val)
            prev = prev.next
            slow = slow.next
        return solution
            
            