class Solution {
    public int romanToInt(String s) 
    {
        int theNumber=0;
        int stringLength = s.length();
        for (int index = 0; index < stringLength;index++)
        {
            {
                if (index != stringLength -1)
                {
                    if(romanToNumber(s.charAt(index)) < romanToNumber(s.charAt(index+1)))
                    {
                        theNumber += romanToNumber(s.charAt(index+1)) - romanToNumber(s.charAt(index));
                        index++;
                    }
                    else
                        theNumber += romanToNumber(s.charAt(index));

                }
                else
                theNumber += romanToNumber(s.charAt(index));
            }
        }

        return theNumber;
        
    }
    public static int romanToNumber(char roman)
    {
        if (roman == 'I')
        return 1;
        if (roman == 'V')
        return 5;
        if (roman == 'X')
        return 10;
        if (roman == 'L')
        return 50;
        if (roman == 'C')
        return 100;
        if (roman == 'D')
        return 500;
        if (roman == 'M')
        return 1000;
        else
        return 0;
        
    }
}