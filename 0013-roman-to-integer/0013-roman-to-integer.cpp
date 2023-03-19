class Solution {
public:
    int romanToInt(string s) 
    {
        int theNumber=0;
        int stringLength = s.size();
        
        for (int index = 0; index < stringLength ;index++)
        {
            {
                if (index != stringLength -1 && romanToNumber(s[index]) < romanToNumber(s[index+1]))
                {
            
                        theNumber += romanToNumber(s[index+1]) - romanToNumber(s[index]);
                        index++;

                }
                else
                theNumber += romanToNumber(s[index]);
            }
        }

        return theNumber;
        
    }
    int romanToNumber(char roman)
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
};