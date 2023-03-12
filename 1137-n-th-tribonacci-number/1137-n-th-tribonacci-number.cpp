class Solution {
public:
    int tribonacci(int n) 
    {
        int n0 = 0;
        int n1 = 1;
        int n2 = 1;
        int temp = 0;
        
        //dealing with some base cases
        if(n == 0)
            return 0;
        
        if (n> 0 && n < 3)
            return 1;
        
        while(n > 2)
        {
            temp = n0;
            n0 =  n1;
            n1 = n2;
            n2 = temp+ n1 + n0;
            
            n--;
        }
        return n2;
        
    }
};