#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    # code here
    i,j = 0,0
    l,h = 0,K-1
    sol = [0]*(N-K+1)#array to store solution
    
    while h < N:
        if i > h:
            j+=1;l+=1;h+=1
        elif A[i]<0 and i > l-1 and i < h+1:
            sol[j] = A[i]
            j+=1;l+=1;h+=1;
        else:
            i+=1
    return sol

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends