# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        linkedlist_len, solution, original_head = 0, [], head
        while head:
            linkedlist_len += 1
            head = head.next
        current = original_head
        if linkedlist_len < k:
            while current:
                solution.append(ListNode(current.val))
                current = current.next
            for i in range(k-linkedlist_len):
                solution.append(None)
        else:
            extras = linkedlist_len%k
            groups = linkedlist_len//k
            
            for i in range(1, k+1):
                if i <= extras:
                    group_len, group_head = groups, current
                    while group_len:
                        current = current.next
                        group_len -= 1
                    prev_next = current.next
                    current.next = None
                    current = prev_next

                    solution.append(group_head)
                else:
                    group_len = groups-1
                    group_head = current
                    while group_len and current:
                        current = current.next
                        group_len -= 1
                    prev_next = current.next
                    current.next = None
                    current = prev_next
                    solution.append(group_head)
        return solution