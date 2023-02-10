	class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int ans = 0, i = 0, j = 0, n = nums.size(),x = 0,a = 0, b = 0;
        while(j<n){
            a = 0, b = 0;
            while(j<n && (x+(nums[j]&1) <= k)){
                x += (nums[j]&1);
                if(x == k){
                    a++;
                }
                j++;
            }
            while(i<n && x == k){
                if(x==k){
                    b++;
                }
                x -= (nums[i]&1);
                i++;
            }
            ans += a*b;
        }
        return ans;
    }
};