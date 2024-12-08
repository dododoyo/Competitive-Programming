# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # use union find 
        rows = len(grid)
        cols = len(grid[0])

        parent = [-1]*(rows*cols)


        def find(i):
            if parent[i] < 0:
                return i 

            parent[i] = find(parent[i])

            return parent[i]

        def union(i,j):
            i_parent = find(i)
            j_parent = find(j)

            if i_parent == j_parent:
                return 
                # cycle 
            
            if parent[i_parent] < parent[j_parent]:
                parent[i_parent] += parent[j_parent]
                parent[j_parent] = i_parent
            else:
                parent[j_parent] += parent[i_parent]
                parent[i_parent] = j_parent


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    current_cell = r*cols + c

                    # connect to upper 
                    if r > 0 and grid[r-1][c]:
                        upper_cell = (r-1)*cols + c
                        union(upper_cell,current_cell)
                    # connect to left
                    if c > 0 and grid[r][c-1]:
                        left_cell = r*cols + (c-1)
                        union(left_cell,current_cell)

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    current_cell = r*cols + c
                    if parent[current_cell] < 0:
                        max_area = max(max_area,abs(parent[current_cell]))
                
        return max_area

                        


        