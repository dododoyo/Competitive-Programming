class Solution {
public:
    double myPow(double x, long long n) 
    {
        if(n== 0 || x == 1)
        return 1;

        if(n < 0)
        return myPow(1/x,abs(n));

        if(x == 0)
        return 0;

        else 
        {
            // if the power is multiple of 2
            // can be replaced by n halfed and x^2
            // x^4 ( where x = x and n = 4)
            // is same as ( x = x^2 and n = 2)
            if (n%2 == 0)
            return myPow(x*x,n/2);

            // if the power is odd 
            // it can be replaced by x*(x^2)^2
            // x^5 is same as x*((x^2)^2)
            else
            return x*myPow(x*x,n/2);

        }
        
    }
};