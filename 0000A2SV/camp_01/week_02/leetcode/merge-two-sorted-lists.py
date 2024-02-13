# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:return list2
        elif list2 == None:return list1
        if list1.val < list2.val:
            merged_list = list1
            list1 = list1.next
        else:
            merged_list = list2
            list2 = list2.next
        tail = merged_list
        while list1 and list2:
            if list1.val < list2.val:
                next_list1 = list1.next
                tail.next = list1
                tail = tail.next
                list1 = next_list1
            else:
                next_list2 = list2.next
                tail.next = list2
                tail = tail.next
                list2 = next_list2
        while list1:
                next_list1 = list1.next
                tail.next = list1
                tail = tail.next
                list1 = next_list1
        while list2:
            next_list2 = list2.next
            tail.next = list2
            tail = tail.next
            list2 = next_list2

        return merged_list
