# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # use a dummy node
        dummy = ListNode(0,head)
        starting_node,window = dummy,right-left+1

        # get the starting node
        while left > 1:
            starting_node = starting_node.next
            left -= 1

        # starting from the starting node move 
        # window steps to get to the ending node
        ending_node = starting_node
        while window:
            ending_node = ending_node.next
            window -= 1

        # register the end and 
        # cut down linkedlist to be reversed
        second_start = ending_node.next
        ending_node.next = None

        # get reversed (ending,starting) nodes
        reversed_start,reversed_end = self.reverseList(starting_node.next)

        starting_node.next = reversed_start
        reversed_end.next = second_start

        return dummy.next

    def reverseList(self,head):
        if head.next == None:
            return head,head
        prev,tail = None,head
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        # prev becomes the new head
        return prev,tail