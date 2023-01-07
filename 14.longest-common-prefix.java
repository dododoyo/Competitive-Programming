class Solution 
{
    public static String longestCommonPrefix(String[] strs) 
    {
        boolean found = false;
        String commonToAll = "";
        String firstString = strs[0];
        int stringLength = firstString.length();
        char currentChar;
        try
        {
            
                for(int i = 0; i < stringLength;i++)
                {
                    currentChar = firstString.charAt(i);
                    for(int j = 0; j < strs.length;j++)
                    {
                        if(currentChar == strs[j].charAt(i))
                            found = true;
                        else
                        {
                            found = false;
                            j = strs.length;
                        }
                    
            
                    }
                    if(found)
                        commonToAll = commonToAll + currentChar;
                    else
                    return commonToAll;
                    
                }
                return commonToAll;
            
        }
        catch (IndexOutOfBoundsException e)
        {
            return commonToAll;
        }
    } 
    
}