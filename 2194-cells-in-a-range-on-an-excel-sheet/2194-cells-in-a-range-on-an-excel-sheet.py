class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        firstColumn = ord(s[0])
        secondColumn = ord(s[3])
        
        firstRow = ord(s[1])
        secondRow = ord(s[4])
        
        solution = []
        
        for i in range(firstColumn, secondColumn + 1):
            for j in range(firstRow, secondRow + 1):
                solution.append(chr(i)+chr(j))
                
        return solution
                
            
            