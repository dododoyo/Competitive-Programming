"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
def getNth(head, k):
    len = 1;
    while head:
        if len == k:return head.data;
        head = head.next
        len +=1 

#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

if __name__ == '__main__':
    llist = LinkedList()
    T = int(input())
    while (T > 0):
        llist = LinkedList()
        n, k = list(map(int, input().split()))
        value = list(map(int, input().split()))
        for i in reversed(value):
            llist.push(int(i))
        m = getNth(llist.head, k)
        print(m)
        T -= 1
        
# Contributed by: Harshit Sidhwa

# } Driver Code Ends