class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0:
                    if col != 0:
                        matrix[row][col] += matrix[row][col-1]
                elif col == 0:
                    matrix[row][col] += matrix[row-1][col]
                else:
                    matrix[row][col] += (matrix[row][col-1]+matrix[row-1][col]-matrix[row-1][col-1])
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = self.matrix[row2][col2]
        if  col1 != 0:summ -= self.matrix[row2][col1-1]
        if  row1 != 0:summ -= self.matrix[row1-1][col2]
        if  row1 != 0 and col1 != 0:summ += self.matrix[row1-1][col1-1]
        return summ

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)