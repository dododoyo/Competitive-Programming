class Solution {
    public void reverseString(char[] s) 
    {
        //use two pointers to flip each value at the end
        
        
        char temp;
        
        for(int p1 = s.length - 1, p2 = 0; p2 < p1; p1 -= 1 , p2 += 1)
        {
            temp= s[p1];
            s[p1] = s[p2];
            s[p2] = temp;
            
        }
    }
}