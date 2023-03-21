class Solution {
public:
    bool isPowerOfTwo(int n) 
    {
        
        // let's use recurssion
        
        //if the number went down two  1 then it is divisible by two
        if(n == 1){return true;}
        
        // if remainder of a number divided by two 
        // is not zero then it is not divisible by two
        if(n == 0 or n%2 != 0){return false;}
        
        //if the number is not one and 
        //not zero and it remainder is zero means its divisible
        //by two check the number all the way down to 1 using recurrsion
        return isPowerOfTwo(n/2);
    }
};