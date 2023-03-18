//{ Driver Code Starts
#include <iostream>
using namespace std;


// } Driver Code Ends
class Solution{
    public:
    // Function to find equilibrium point in the array.
    // a: input array
    // n: size of array
    int equilibriumPoint(long long a[], int n) 
    {
        int sum1 [n] = {0}; 
        int sum2 [n] = {0}; 
        
        if(n==1)
        {
            return 1;
        }
    
        sum1[0] = a[0];
        for(int i = 1 ; i < n; i++)
        {
            sum1[i] = a[i] + sum1[i-1];
        }
        
        
        sum2[n-1] = a[n-1];
        for(int i = n-2 ; i > -1; i--)
        {
            sum2[i] = a[i] + sum2[i+1];
        }
        
        
        for(int i = 1 ; i < n; i++)
        {
            if(sum1[i-1] == sum2[i+1])
            {
                return i+1;
            } 
        }
        
        return -1;
           
        // Your code here
    }

};

//{ Driver Code Starts.


int main() {

    long long t;
    
    //taking testcases
    cin >> t;

    while (t--) {
        long long n;
        
        //taking input n
        cin >> n;
        long long a[n];

        //adding elements to the array
        for (long long i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        Solution ob;

        //calling equilibriumPoint() function
        cout << ob.equilibriumPoint(a, n) << endl;
    }
    return 0;
}

// } Driver Code Ends