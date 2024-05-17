# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last_row = [1]*m
        last_column = [1]*n

        for i in range(1,m):
            for j in range(1,n):
                current_paths = last_row[i] + last_column[j]
                last_column[j] = current_paths
                last_row[i] = current_paths

        # space = O(n+m) time = O(n*m)
        return last_row[m-1]