# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst=[]
        for i in lists:
            while i:
                lst.append(i.val)
                i=i.next
        lst.sort()
        a=ListNode(0)
        tmp=a
        for i in lst:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return a.next