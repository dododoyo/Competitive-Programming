class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkColumns(board) and self.checkRows(board) and self.checkSubBoxes(board)     
    def checkColumns(self,board):
        for i in range(9):
            freq_counter = [0]*9
            for j in range(9):
                if board[j][i] != ".":freq_counter[int(board[j][i])-1] +=1
            if not self.validFrequency(freq_counter):return False
        return True
    def checkRows(self,board):
        for i in range(9):
            freq_counter = [0]*9
            for j in range(9):
                if board[i][j] != ".":freq_counter[int(board[i][j])-1] +=1
            if not self.validFrequency(freq_counter):return False
        return True
    def checkSubBoxes(self,board):
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not self.checkSubBox(board,i,j):return False
                print()
        return True
    def checkSubBox(self,board,row,col):
        freq_counter = [0]*9
        for i in range(row,row+3):
            for j in range(col,col+3):
                if board[i][j] != ".":freq_counter[int(board[i][j])-1] +=1
            if not self.validFrequency(freq_counter):
                return False

        return True    
    def validFrequency(self,freq_arr):
        for i in freq_arr:
            if i > 1:return False
        return True
        