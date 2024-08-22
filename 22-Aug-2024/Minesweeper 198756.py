# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        row, col = len(board), len(board[0])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        def dfs(click):
            i,j = click
            if board[i][j] != 'E':
                return

            row, col = len(board), len(board[0])       
            MOVES = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

            mines = 0

            for dx,dy in MOVES:
                x, y = i + dx, j + dy
                if 0 <= x < row and 0 <= y < col and board[x][y] == 'M':        
                    mines += 1

            if mines == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(mines)
                return

            for dx,dy in MOVES:
                x, y = i + dx, j + dy
                if 0 <= x < row and 0 <= y < col:
                    dfs([x,y])

        dfs(click)

        return board