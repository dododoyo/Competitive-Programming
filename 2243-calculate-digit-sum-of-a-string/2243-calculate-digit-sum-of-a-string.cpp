class Solution {
public:
    string digitSum(string s, int k) 
    {
        int s_int = 0;
        int l = 0;
        int sub = 1;
        string total_s = "";
        while(s.size() > k)
        {
            while(l < s.size())
            {
                while(l < sub*k && l < s.size())
                {
                    s_int += int(s[l]) - 48;
                    l++;   
                }
                
                total_s = total_s + to_string(s_int);//
                s_int = 0;
                sub++;
            }
            s = total_s;
            l = 0;
            total_s = "";
            sub = 1;
        }
        
        return s;
        
    }
};