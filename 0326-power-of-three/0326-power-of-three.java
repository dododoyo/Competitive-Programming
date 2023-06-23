class Solution {
    public boolean isPowerOfThree(int n) 
    {
        // true if goes down to '1'
        if (n==1){return true;}
        // false if n is zero or remainder is not zero
        if (n==0 || n%3!=0){return false;}
        return isPowerOfThree(n/3);
        
    }
}