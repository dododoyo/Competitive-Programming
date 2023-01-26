/*
 * @lc app=leetcode id=155 lang=java
 *
 * [155] Min Stack
 */

// @lc code=start
import java.util.*;
class MinStack {

    Stack<Integer> theStack; 
    Stack<Integer> minStack;

    public MinStack() 
    {
        theStack = new Stack<>();
        minStack = new Stack<>();
        
    }
    
    public void push(int val) 
    {
        // if stack used to collect minimums is empty don't check 
        // for anything just add the current value to the minStack

        // or if new added value is less than the current minimum 
        // make the new minimum the new value.
        if(minStack.isEmpty() || val <= minStack.peek())
        {
            minStack.push(val);
        }   
        // either way new value must be pushed to the stack
        theStack.push(val);
        
    }
    
    public void pop() 
    {
        // if object to be poped is the minimum value then we have 
        // to remove it from the minStack also because it is no longer the minimum

        if(theStack.peek().equals(minStack.peek()))
        {
            
            minStack.pop();
        }

        // pop element in the stack anyway
        theStack.pop();
        
    }
    
    public int top() {
        return theStack.peek();
        
    }
    
    public int getMin() 
    {
        return minStack.peek();
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
// @lc code=end

