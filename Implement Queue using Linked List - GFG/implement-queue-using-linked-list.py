# A linked list (LL) node 
# to store a queue entry 


class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None

    #Function to push an element into the queue.
    def push(self, item): 
        item_node = Node(item)
        #if the list is empty then both the head and the tail point at the start
        if self.head is None or self.tail is None:
            self.head = item_node
            self.tail = item_node
        # if not head is still unchanged because we are appending to the end 
        # but new node is the last node so we point tail will point to it
        else:
            self.tail.next = item_node
            self.tail = self.tail.next
            
    
    #Function to pop front element from the queue.
    def pop(self):
        # if the list is empty? return -1
        if self.head is None:
            return -1
        # get the item from the last head because it will be changed once we pop it
        # and make the new node to the one beside it 
        item = self.head.data
        self.head = self.head.next
        
        return item 


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends