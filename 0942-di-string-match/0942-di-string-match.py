class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        str_arr = list(s)
        all_elements = list(range(len(s)+1))
        solution = []
        for i in range(len(str_arr)):
            if(s[i] == "I"):
                solution.append(all_elements[0])
                all_elements.remove(all_elements[0])
            elif(s[i] == "D"):
                solution.append(all_elements[-1])
                all_elements.pop()
    
            
        while(len(all_elements) != 0):
            solution.append(all_elements.pop())
        
        return solution