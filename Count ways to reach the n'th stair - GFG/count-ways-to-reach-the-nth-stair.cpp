//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    public:
    //Function to count number of ways to reach the nth stair.
    int countWays(int n)
    {
        if (n == 1){return 1;}
        if (n == 2){return 2;}
        
        long long sum_0 = 1;
        int i = 0;
        int sum_1 = 2;
        int const divisor = 1e9+7;
        while(i<n-2)
        {
            sum_1 = sum_1 + sum_0;
            sum_0 = sum_1 - sum_0;
            sum_1 %= divisor;
            i++;
        }
        return sum_1;
        
        
    }
};



//{ Driver Code Starts.
int main()
{
    //taking total testcases
    int t;
    cin >> t;
    while(t--)
    {
        //taking stair count
        int m;
        cin>>m;
        Solution ob;
        cout<<ob.countWays(m)<<endl; // Print the output from our pre computed array
    }
    return 0;
}

// } Driver Code Ends