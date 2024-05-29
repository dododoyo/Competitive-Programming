# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(n):
            for pre in ingredients[i]:
                graph[pre].append(recipes[i])
                indegree[recipes[i]] += 1
        
        bfs_que = supplies[:]
        solution = []

        while bfs_que:
            next_que = []
            for node in bfs_que:
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        solution.append(neighbor)
                        next_que.append(neighbor)

            bfs_que = next_que[:]

        return solution
