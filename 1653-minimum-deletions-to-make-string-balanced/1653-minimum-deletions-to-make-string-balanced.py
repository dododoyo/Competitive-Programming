class Solution:
    def minimumDeletions(self, s):
        #ans counts the number of b's that occured before a's
        ans = 0
        
        #count counts the number of b's that occured before a in our substring
        #going from left to right
        
        count = 0
        
        #we go througth each element of the string
        for i in s:
            
            #if the current character is 'b'  we count it 
            if i == 'b':
                count += 1
                
            # if it is not 'b' and b has occured before it
            # remove it from our count(string) and increase answer
            elif count:
                ans += 1
                count -= 1
                
        return ans