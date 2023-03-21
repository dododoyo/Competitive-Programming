class Solution {
public:
    bool isPowerOfTwo(int n) 
    {
        if(n < 0)
            return false;
    
        while(n>1)
        {
            if(n%2 == 0)
            {
                n = n/2;
            }
            else
            {
                return false;
            }
        }
        
        if(n== 0)
            return false;
    
        return true;
        
    }
};