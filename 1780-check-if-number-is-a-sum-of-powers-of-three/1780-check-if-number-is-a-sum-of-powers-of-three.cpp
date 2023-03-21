class Solution {
public:
    bool checkPowersOfThree(int n) 
    {
        if(n == 1){return true;}
        if(n%3 > 1 or n == 0){return false;}
        return checkPowersOfThree(n/3);
        
    }
};