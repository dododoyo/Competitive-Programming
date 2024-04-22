# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k, min_heap, counter= len(lists), [], 0
        for i in range(k):
            current_head = lists[i]
            while current_head:
                heapq.heappush(min_heap,[current_head.val,counter,current_head])
                current_head,counter = current_head.next,counter+1
    
        dummy = ListNode(0)
        current_node = dummy

        while min_heap:
            current_node.next = heapq.heappop(min_heap)[2]
            current_node = current_node.next

        return dummy.next
        
