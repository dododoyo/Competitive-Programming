class Solution {
public:
    int getLucky(string s, int k) 
    {
        int string_len = s.size();
        string int_str = "";
        int int_size = 0;
        
        //first tranformation
        for(int i = 0; i < string_len;i++)
        {
            int_str += to_string(int(s[i]) - 96);
        }
        cout<<int_str;
        
        int operation = 0;
        long long each_int = 0;
        
        //second transformation
        while(operation < k)
        {
            int_size = int_str.size();
            for(int i = 0; i<int_size;i++)
            {
                // subtracting 48 beacuse int gives ascii value
                each_int += int(int_str[i]) - 48;
            }
            operation++;
            int_str = to_string(each_int);
            each_int = 0;
        }  
        return stoi(int_str);    
    }
};