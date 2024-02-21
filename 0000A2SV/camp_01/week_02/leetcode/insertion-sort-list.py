# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        original_head = head
        dummy = ListNode(-5001,head)
        current = head.next
        while current:
            # get it's value
            current_value = current.val

            # remove it 
            if current.next:
                current.val = current.next.val
                current.next = current.next.next
            else:
                current = None

            # find it's right place
            start = dummy
            while start and start.next and start.next.val < current_value:
                start = start.next

            # insert it 
            prev_point = start.next
            start.next = ListNode(current_value,prev_point)
        current = original_head
        while current and current.next and current.next.next:
            print(current.val)
            current = current.next
        current.next = None
        return dummy.next