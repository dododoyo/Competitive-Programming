class Solution {
    public boolean judgeCircle(String moves) 
    {

        int upCounter = 0;
        int downCounter = 0;
        int leftCounter = 0;
        int rightCounter = 0;
        for(int i = 0; i < moves.length() ; i++)
        {
            if (moves.charAt(i) == 'L')
            leftCounter++;
            else if (moves.charAt(i) == 'U')
            upCounter++;
            else if (moves.charAt(i) == 'D')
            downCounter++;
            else if (moves.charAt(i) == 'R')
            rightCounter++;

        }

        if (downCounter == upCounter && leftCounter == rightCounter)
        return true;
        else;
        return false;
        
    }
}
// @lc code=end

