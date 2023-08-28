class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #iterative solution
        sol = [[1]]
        
        for i in range(rowIndex):
            temp = [0]+sol[-1]+[0];
            curr = [0]*(len(temp)-1);
            for j in range(len(curr)):
                curr[j] = temp[j] + temp[j+1];
            sol.append(curr);
        
        return sol[-1]
        
        
        
        