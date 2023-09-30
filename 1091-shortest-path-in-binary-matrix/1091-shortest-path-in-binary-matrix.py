class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1

        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, length in q:
            if i == n-1 and j == n-1: return length
            for dx, dy in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= dx < n and 0 <= dy < n and not grid[dx][dy]:
                    grid[dx][dy] = 1
                    q.append((dx, dy, length+1))
        return -1