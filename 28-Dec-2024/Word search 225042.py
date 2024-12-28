# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:    
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for each cell in the greed we can assume 
        # it is the starting point of the string 
        m = len(board)
        n = len(board[0])
        seen = set()
        MOVES = [(1,0),(0,1),(-1,0),(0,-1)]

        def find_word(r,c,index):
            if index == len(word):
                return True 

            if (r,c) in seen:
                return False 
            
            if not (-1 < r < m and -1 < c < n):
                return False 

            if board[r][c] != word[index]:
                return False

            seen.add((r,c))

            for dx,dy in MOVES:
                x,y = dx+r,dy+c
                if find_word(x,y,index+1):
                    return True

            seen.remove((r,c))
            return False
            

        for i in range(m):
            for j in range(n):
                if find_word(i,j,0):
                    return True

        return False