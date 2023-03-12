class Solution {
public:
    int climbStairs(int n) 
    {
        if (n < 3)
            return n;
        
        
        int prev_prev = 1;
        int prev = 2;
        
        /* the trick is that the result of the nth step is the summation of the 
        previous two steps just like fibonacci sequence
        we might use recurrsion but that will take more time*/
        
        while(n > 2)
        {
            prev = prev + prev_prev;
            prev_prev = prev - prev_prev;
            n--;
        }
        return prev;
        
    }
};