class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) 
    {
        vector<int> freq(101);   
        for(int i = 0; i < nums.size();i++){freq[nums[i]] += 1;}
        for(int i = 1; i < freq.size();i++){freq[i] = freq[i] + freq[i-1];}
        vector<int> solution;
        if(freq[target] > 0)
        {
            for(int i = freq[target-1] ; i < freq[target];i++)                                                  {solution.insert(solution.end(),i);}
        }
        else{return solution;}
        
        return solution;
    }
};