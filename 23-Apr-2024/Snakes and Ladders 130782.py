# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def intToPos(nghbr):
            row = (nghbr-1)//n
            column = (nghbr-1)%n

            if row%2: # row is odd
                column = n - (1+column) 
            return row,column

        current_level,visited = [1],set()
        level_count = 1

        while current_level:
            next_level = []
            for node in current_level:
                for i in range(1,7):
                    nghbr = node + i
                    r,c = intToPos(nghbr)

                    if board[r][c] != -1:
                        nghbr = board[r][c]
                    
                    if nghbr == n*n:
                        return level_count 
                    
                    if nghbr not in visited:
                        visited.add(nghbr)
                        next_level.append(nghbr)
            level_count += 1
            current_level = next_level
            
        return -1

        