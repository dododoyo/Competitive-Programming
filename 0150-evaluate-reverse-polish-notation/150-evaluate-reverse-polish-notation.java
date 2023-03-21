import java.util.*;
class Solution 
{
    public int evalRPN(String[] tokens) 
    {
        if(tokens.length == 1)
            return Integer.parseInt(tokens[0]);
        
        Stack<Integer> numStack = new Stack<Integer>();
        int firstPopped;
        for(String val: tokens)
        {
            if(val.equals("*"))
            {
                firstPopped = numStack.pop();
                numStack.push(numStack.pop()*firstPopped);
            }
            else if(val.equals("/"))
            {
                firstPopped = numStack.pop();
                numStack.push(numStack.pop()/firstPopped);
            }
            else if(val.equals("-"))
            {
                firstPopped = numStack.pop();
                numStack.push(numStack.pop()-firstPopped);
            }
            else if(val.equals("+"))
            {
                firstPopped = numStack.pop();
                numStack.push(numStack.pop()+firstPopped);
            }
            else
            numStack.push(Integer.parseInt(val));
        }
        return numStack.pop();
    }
}
// @lc code=end

