# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board):
        current_level, seen = [], set()
        n, m = len(board), len(board[0])
        MOVES = [(0,1),(0,-1),(1,0),(-1,0)]

        for r in range(n):
            for c in range(m):
                # if "O"s are on the boundary  they cant be surrouneded
                # mark any of their neighbors with "M"
                if ((r in [0, n-1]) or (c in [0, m-1])) and board[r][c] == "O":
                    current_level.append((r,c))
                    seen.add((r,c))

        while current_level:
            next_level = []

            for node in current_level:
                i,j = node
                board[i][j] = "M"
                for dx,dy in MOVES:
                    x,y = dx+i,dy+j
                    if (-1 < x < n) and (-1 < y < m) and ((x,y) not in seen) and (board[x][y] == "O"):
                        next_level.append((x,y))
                        seen.add((x,y))

            current_level = next_level[:]
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == "M":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

        return board