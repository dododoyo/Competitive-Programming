class Solution {
    public List<Integer> findAnagrams(String s, String p) 
    {
        int size_S = s.length();
        int size_P = p.length();
        ArrayList<Integer> solution = new ArrayList<Integer>();
        for(int i = 0 ; i < (size_S - size_P)+1; i++)
        {
            if(isAnagram(p,s.substring(i,i+size_P)))
                solution.add(i);
        }
        return solution;
    }
    
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