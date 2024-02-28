class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # make the changes such that for each row and
        # each column the maximum value must stay the same

        # for each cell we can change it into the minimum 
        # of the maximums in it's grid
        n = len(grid)
        rows_max = [0]*n
        for i in range(n):
            rows_max[i] = max(grid[i])
        columns_max = [0]*n
        prev_sum = 0
        for i in range(n):
            column_max = grid[0][i]
            for j in range(n):
                prev_sum += grid[j][i]
                column_max = max(column_max,grid[j][i])
            columns_max[i] = column_max
        solution = 0
        for i in range(n):
            for j in range(n):
                # print(min(rows_max[i], columns_max[j]))
                print(rows_max[i], columns_max[j])
                solution += min(rows_max[i], columns_max[j])
        return solution - prev_sum