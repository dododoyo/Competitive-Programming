# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge case if the node is only one remove it
        if head.next == None:return None
        fast,slow = head.next.next,head
        #loop to detect end and middle of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #code to remove middle
        slow.next = slow.next.next
        return head