class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)%2:
            center_element = mat[len(mat)//2][len(mat)//2]
            return self.getDiagonals(mat) - center_element
        else:
            return self.getDiagonals(mat)
    def getDiagonals(self,mat):
        primary,secondary = 0,0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i-j == 0:primary += mat[i][j]
                if i+j == len(mat)-1:secondary += mat[i][j]
        return primary+secondary
