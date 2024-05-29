# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        solution = [-1]*len(queries)

        for index,query in enumerate(queries):
            a,b = query
            if a == b:
                solution[index] = a
            elif heights[max(a, b)] > heights[min(a, b)]:
                solution[index] = max(a, b)

        new_heights = []
        for i, (a, b) in enumerate(queries):
            if solution[i] == -1:
                new_heights.append((max(a, b), max(heights[a], heights[b]), i) )

        queries = sorted(new_heights)[::-1]

        s = []
        for i, height, index in queries:
            while i + 1 < len(heights):
                top = heights.pop()
                while s and -s[-1][0] <= top:
                    s.pop()
                s.append((-top, len(heights)))
            vld = bisect_left(s, (-height, -1)) - 1

            if vld >= 0:
                solution[index] = s[vld][1]
        return solution        