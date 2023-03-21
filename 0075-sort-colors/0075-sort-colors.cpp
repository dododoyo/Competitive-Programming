class Solution {
public:
    void sortColors(vector<int>& nums) 
    {
        int numOfZeros = 0,numOfOnes = 0,numOfTwos = 0;
            
        for(int i = 0 ; i< nums.size(); i++)
        {
            numOfZeros+=(nums[i]==0);
            numOfOnes+=(nums[i]==1);
            numOfTwos+=(nums[i]==2);
        }
        int index = 0;
        while(numOfZeros > 0){nums[index] = 0;index++;numOfZeros--;}
        while(numOfOnes > 0){nums[index] = 1;index++;numOfOnes--;}
        while(numOfTwos > 0){nums[index] = 2;index++;numOfTwos--;}
    }
};