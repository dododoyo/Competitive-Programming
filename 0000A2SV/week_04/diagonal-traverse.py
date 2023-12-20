from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal_map = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):diagonal_map[row+col].append([row,col])
        solution = []
        for diagonal in diagonal_map.keys():
            if diagonal %2:
                for element in diagonal_map[diagonal]:
                    solution.append(mat[element[0]][element[1]])
            else:
                for index in range(len(diagonal_map[diagonal])-1,-1,-1):
                    diagonal_element = diagonal_map[diagonal][index]
                    solution.append(mat[diagonal_element[0]][diagonal_element[1]])
        return solution
        