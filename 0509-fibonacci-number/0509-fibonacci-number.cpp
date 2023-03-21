class Solution {
public:
    int fib(int n) 
    {
        if(n == 0)
            return 0;
        if(n == 1)
            return 1;
        
        int i0 = 0;
        int i1 = 1;
        
        while(n > 1)
        {
            i1 = i0 + i1;
            i0 = i1 - i0;
            n -= 1;
        }
        
        return i1;
    }
};