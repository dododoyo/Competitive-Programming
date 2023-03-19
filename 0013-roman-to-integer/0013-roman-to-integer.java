import java.util.*;
class Solution {
    public int romanToInt(String s) 
    {
        int s_len = s.length();
        HashMap<Character, Integer> romanMap = new HashMap<>(); 
        romanMap.put('I',1);
        romanMap.put('V',5);
        romanMap.put('X',10);
        romanMap.put('L',50);
        romanMap.put('C',100);
        romanMap.put('D',500);
        romanMap.put('M',1000);
        
        int solution = 0;
        int i = 0;
        while(i < s_len)
        {
            if(i != (s_len - 1) && romanMap.get(s.charAt(i)) < romanMap.get(s.charAt(i+1)) )
            {
                solution += romanMap.get(s.charAt(i+1)) - romanMap.get(s.charAt(i));
                i += 2; 
            }
            else
            {
                solution += romanMap.get(s.charAt(i));
                i++;   
            }
            
        }
        return solution;
    }
}