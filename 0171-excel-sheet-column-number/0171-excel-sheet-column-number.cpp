class Solution {
public:
    int titleToNumber(string columnTitle) 
    {
        int str_length = columnTitle.size();
        long solution = 0;
        
        for(int i = 0; i < str_length ; i++)
            solution = solution*26 + int(columnTitle[i]) - 64;
        
        return solution;
    }
};