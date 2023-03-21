class Solution {
public:
    void sortColors(vector<int>& nums) 
    {
        int freqArr[3] = {0};
        
    
        for(int i = 0; i < nums.size() ; i++){freqArr[nums[i]]++;}
        for(int i = 1; i < 3 ; i++){freqArr[i] = freqArr[i] + freqArr[i-1];}
        int* solution = new int[nums.size()];
        for(int i = 0 ; i<nums.size();i++){solution[--freqArr[nums[i]]] = nums[i];}
        for(int i = 0 ; i<nums.size();i++){nums[i] = solution[i];}
    }
};