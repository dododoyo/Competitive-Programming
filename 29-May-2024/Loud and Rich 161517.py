# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        richer_than = [[] for _ in range(n)]

        for a, b in richer:
            richer_than[b].append(a)

        solution = [None] * n

        def dfs(node):
            if solution[node] is None:
                solution[node] = node

                for child in richer_than[node]:
                    candidate = dfs(child)

                    if quiet[candidate] < quiet[solution[node]]:
                        solution[node] = candidate

            return solution[node]

        return list(map(dfs, range(n)))