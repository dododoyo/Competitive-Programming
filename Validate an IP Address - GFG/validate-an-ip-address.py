#User function Template for python3
def isValid(s):
    #code here
    
    #checking if input starts  and ends with "."
    
    if s[0] == '.' or s[-1] == ".":
        return 0
        
    each_IP = s.split(".")
    
    len_ = len(each_IP)
    
    #testing if string doesn't contain 4 numbers
    if(len_ != 4):
        return 0
    
    for i in range(len_):
        
        each_str = each_IP[i]
        
        #testing for empty strings
        if each_str == "":
            return 0
            
        #testing if strings are not numbers
        if not each_str.isnumeric():
            return 0
            
        #testing for leading zeros
        if (len(each_str) > 1) and (each_str[0] == "0"):
            return 0
            
        each_num = int(each_str)
        
        #testing if each nums is within range
        if (each_num > 255 or each_num < 0 ): 
            return 0
            
    return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends