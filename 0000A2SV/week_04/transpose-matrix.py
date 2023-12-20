class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        solution = []
        for i in range(len(matrix[0])):
            new_row = [0]*len(matrix)
            for j in range(len(matrix)):
                new_row[j] = matrix[j][i]
            solution.append(new_row)
        return solution
        