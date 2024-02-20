# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(list1,list2)

    def helper(self, list1, list2):
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val < list2.val:
                list1.next = self.helper(list1.next, list2)
                return list1
            else:
                list2.next = self.helper(list1, list2.next)
                return list2