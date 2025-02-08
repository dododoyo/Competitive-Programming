# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def isValid(self,r,c):
        return (-1 < r < self.rows) and (-1 < c < self.cols)

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        self.rows = len(img)
        self.cols = len(img[0])

        MOVES = [(0,-1),(0,0),(0,1),
                 (-1,-1),(-1,0),(-1,1),
                 (1,-1),(1,0),(1,1)]

        solution = [[0 for i in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                summ = 0
                count = 0 
                for dx,dy in MOVES:
                    x,y = dx+r,dy+c

                    if self.isValid(x,y):
                        summ += img[x][y]
                        count += 1 

                solution[r][c] = summ//count

        
        return solution