class Solution {
public:
    string convertToTitle(int columnNumber) 
    {
        string solution = "";
        
        while(columnNumber > 0)
        {
            columnNumber--;
            solution = char(columnNumber%26 + 65) + solution;
            columnNumber /= 26;
        
        }
        return  solution;
    }
    
};