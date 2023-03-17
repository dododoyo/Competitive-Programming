//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

long long int no_of_subarrays(int n, vector<int> &arr) {
    // Write your code here.
    
    // to solve this we will got through the array
    //     until we get a 1 then we can calculate 
    //     the number of subarrays that can be formed
    //     from each subarray of zeros
    
    // time O(n)
    // space O(1)
    
    
    long zeros = 0;
    long total_sub = 0;
    int i = 0;
    
    while(i < n)
    {
        while(arr[i] == 0 && i < n)
        {
            zeros++;
            i++;
        }
        total_sub += (zeros*(zeros+1))/2;
        zeros = 0;
        i++;
    }
    
    return total_sub;
}

//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        cout << no_of_subarrays(n, arr) << endl;
    }
}

// } Driver Code Ends