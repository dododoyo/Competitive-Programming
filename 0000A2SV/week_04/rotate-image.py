class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        # print(matrix)
        self.invert(matrix)
        
    def transpose(self,matrix):
        last_row = 1
        for i in range(len(matrix)-1):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
            

    def invert(self,matrix):
        for i in range(len(matrix)):
            left,right = 0,len(matrix)-1
            while left < right:
                matrix[i][left],matrix[i][right] = matrix[i][right],matrix[i][left]
                left,right = left+1,right-1
        