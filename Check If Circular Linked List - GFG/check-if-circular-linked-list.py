#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    slow = head;
    fast = head;
    while (slow != None) and (fast != None) and (fast.next != None):
        slow = slow.next;
        fast = fast.next.next;
        if slow == fast:return 1;
    return 0;
    # Code here



#{ 
 # Driver Code Starts
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self, node):
        temp = node
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def getHead(self):
        return self.head

    def createLoop(self, n):
        if n == 0:
            return None
        temp = self.head
        ptr = self.head
        cnt = 1
        while (cnt != n):
            ptr = ptr.next
            cnt += 1
        # print ptr.data
        while (temp.next):
            temp = temp.next
        temp.next = ptr

# Driver program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n,isloop = list(map(int, input().strip().split()))
        arr=list(map(int, input().strip().split()))
        lst=LinkedList()
        for i in arr:
            lst.push(i)
        if(isloop):
            lst.createLoop(1)
        if isCircular(lst.getHead()):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa
# } Driver Code Ends