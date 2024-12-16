# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # use iteration 
        if not head:
            return head
        node = Node(-1,head)

        curr_node = node.next 

        # copy all nodes with their next node 
        # and insert the copies between the old ones
        while curr_node:
            copy = Node(curr_node.val)
            copy.next=curr_node.next
            curr_node.next = copy
            curr_node = copy.next
            
        curr_node = node.next
        # copy the random pointers
        while curr_node:
            copy = curr_node.next
            if curr_node.random:
                copy.random = curr_node.random.next
            else:
                copy.random = None

            curr_node = curr_node.next.next

        old_list = node.next
        new_list = node.next.next
        new_head = new_list

        while old_list:
            # detach old list
            old_list.next = old_list.next.next

            # detach new_list
            if new_list.next:new_list.next = new_list.next.next
            else:new_list.next = None

            # register next pointer
            old_list = old_list.next
            new_list = new_list.next

        return new_head