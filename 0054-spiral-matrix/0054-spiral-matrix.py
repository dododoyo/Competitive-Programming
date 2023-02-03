class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startRow = 0
        startCol = 0
        
        endRow = len(matrix)
        endCol = len(matrix[0])
        
        answer = []
        
        while (startRow<endRow and startCol <endCol):
            for i in range(startCol,endCol):
                answer.append(matrix[startRow][i])
                
            startRow +=1
            
            for i in range(startRow,endRow):
                answer.append(matrix[i][endCol-1])
                
            endCol -=1
            
            if not(startCol<endCol and startRow <endRow):
                break
            
            for i in range(endCol-1,startCol-1,-1):
                answer.append(matrix[endRow-1][i])
                
            endRow -=1
            
            for i in range(endRow-1,startRow-1,-1):
                answer.append(matrix[i][startCol])
                
            startCol+=1
            
        return answer
                
            
        