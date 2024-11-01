# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n, m = len(targetGrid), len(targetGrid[0])
        colors = set()
        min_row, max_row, min_col, max_col = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)

        for row in range(n):
            for col in range(m):
                color = targetGrid[row][col]
                if color not in colors:
                    min_row[color] = row
                    max_row[color] = row
                    min_col[color] = col
                    max_col[color] = col
                    colors.add(color)
                else:
                    min_row[color] = min(min_row[color], row)
                    max_row[color] = max(max_row[color], row)
                    min_col[color] = min(min_col[color], col)
                    max_col[color] = max(max_col[color], col)

        graph = defaultdict(list)
        indegree = defaultdict(int)

        for color in colors:
            visited = set([color])
            for row in range(min_row[color], max_row[color] + 1):
                for col in range(min_col[color], max_col[color] + 1):

                    if targetGrid[row][col] not in visited:
                        visited.add(targetGrid[row][col])
                        graph[color].append(targetGrid[row][col])
                        indegree[targetGrid[row][col]] += 1
        queue = deque()
        current_level = []
        for color in colors:
            if indegree[color] == 0:
                queue.append(color)
                current_level.append(color)

        solution = 0
        while current_level:
            solution += len(current_level)
            next_level = []
            for node in current_level:
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        next_level.append(neighbor)

            current_level = next_level[:]
        
        return True if solution == len(colors) else False