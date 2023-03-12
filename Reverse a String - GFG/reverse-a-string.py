#User function Template for python3

def reverseWord(s):
    #your code here
    pointer = len(s) - 1
    solution = ""
    for i in range(pointer,-1,-1):
        solution += s[i]
    
    return solution


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends