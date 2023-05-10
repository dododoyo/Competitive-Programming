#User function Template for python3



#Function to generate binary numbers from 1 to N using a queue.
def generate(N):
    sol2 = [""]*N
    for i in range(1,N+1):
        sol2[i-1] = to_binary(i)
    return sol2
def to_binary(num):
    sol = []
    while(num>0):
        sol.append(str(num%2))
        num = num//2
        
    return "".join(sol[::-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by :  Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
# } Driver Code Ends