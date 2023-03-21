class Solution {
public:
    int findGCD(vector<int>& nums) 
    {
        int themin = nums[0];
        for(int i = 0; i< nums.size();i++){if(nums[i] < themin)themin = nums[i];}
        int themax = nums[0];
        for(int i = 0; i< nums.size();i++){if(nums[i] > themax)themax = nums[i];}
        
        int solution = 1;
        int gcd = 1;
        
        while(gcd < themin+1)
        {
            if(themin%gcd == 0 and themax%gcd == 0){solution = gcd;}
            gcd++;
            
        }
    
        return solution;
    }
};