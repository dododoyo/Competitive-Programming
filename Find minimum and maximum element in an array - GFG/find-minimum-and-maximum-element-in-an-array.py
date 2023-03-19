#User function Template for python3

def getMinMax( a, n):
    min_ = a[0]
    max_ = a[0]
    
    for i in a:
        if i < min_:
            min_ = i
            
        if i > max_:
            max_ = i
            
    return min_,max_
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends