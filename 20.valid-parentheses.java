
import java.util.HashMap;
import java.util.Stack;

/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution 
{
    public boolean isValid(String s) 
    {
        HashMap<Character,Character> bracketsMap = new HashMap<>();
        bracketsMap.put(']', '[');
        bracketsMap.put(')','(');
        bracketsMap.put('}', '{');
        char[] characterArray = s.toCharArray();
        Stack<Character> theStack = new Stack<>();
        if (s.length() == 1)
        return false;

        for (char value : characterArray)
        {
            if ( value == '(' || value == '{' || value == '[')
            {
                theStack.push(value);
            }
            else
            {
                if(!theStack.empty())
                {
                    if (theStack.pop() == bracketsMap.get(value))
                    continue;
                    
                    else return false;
                }
                else
                return false;
            }
        } return theStack.empty();
        
    }
}
// @lc code=end

