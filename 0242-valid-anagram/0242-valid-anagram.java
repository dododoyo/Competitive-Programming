class Solution 
{
    public boolean isAnagram(String s, String t) 
    {
        int s_len = s.length();
        int t_len = t.length();
        
        if(s_len != t_len)
            return false;
        
        int[] counter = new int[26];
        
        for(int i = 0 ; i < s_len ; i++)
        {
            counter[(int)(s.charAt(i))-97] += 1;
        }
        
        for(int i = 0 ; i < t_len ; i++)
        {
            counter[(int)(t.charAt(i))-97] -= 1;
        }
        
        for(int i : counter)
        {
            if(i != 0)
                return false;
        }
        
        return true;
        
        
        
    }
}