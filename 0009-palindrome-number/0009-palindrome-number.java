class Solution {
    public boolean isPalindrome(int x) 
    {
        int newNumber =0 ,result,temp = x;
        if (x < 0)
        x *= -1;
        
        while(x!=0)
        {
            result = x%10;
            newNumber = newNumber*10 + result;
            x = x /10;
        }  

        if (temp == newNumber)
            return true;
        else
            return false;
    }
}