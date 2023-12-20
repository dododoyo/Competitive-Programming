class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        solution = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                solution = max(solution,self.getSum(row,col,grid))
        return solution

    def getSum(self, row:int ,col:int ,grid:List[List[int]])-> int:
        hourglass_elements = [[row,col],[row,col+1],[row,col+2],[row+1,col+1],[row+2,col],[row+2,col+1],[row+2,col+2]]
        hourglass_sum = 0
        for element in hourglass_elements:
            hourglass_sum += grid[element[0]][element[1]]
        return hourglass_sum
        