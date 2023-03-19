class Solution:
    def removeDuplicateLetters(self,s: str) -> str:
        solution = []
        
        #use an array to count the occurence of each character
        #since all elements are small letters can use finite sized array
        chr_frq = [0]*26

        for i in s:
            chr_frq[ord(i)-97] += 1
        
        #use a flag array to see if an element is already inserted in the solution
        
        seen = [False]*26
        
        # we will generally have two cases either chracter was seen before or not
        for i in range(len(s)):
            order = ord(s[i])

            if(seen[order-97]):
                chr_frq[order-97] -= 1
                continue
            
            while(len(solution) != 0 and solution[-1] > s[i] and chr_frq[ord(solution[-1])-97] != 0):
                seen[ord(solution[-1])-97] = False
                solution.pop()
                
            solution.append(s[i])
            seen[order-97] = True
            chr_frq[order-97] -= 1
            
        return "".join(solution)

