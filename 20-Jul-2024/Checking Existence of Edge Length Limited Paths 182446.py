# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = {i:i for i in range(n)}
        rank = [1]*n
        edgeList.sort(key = lambda x:x[2])

        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x

        def union(x, y):
            root1, root2 = find(x), find(y)
            if rank[root1] > rank[root2]:
                parents[root2] = parents[root1]
            elif rank[root1] < rank[root2]:
                parents[root1] = parents[root2]
            else:
                parents[root1] = parents[root2]
                rank[root2] += 1
        def isConnected(x, y):
            return find(x) == find(y)

        indices = {tuple(q): i for i, q in enumerate(queries)}
        queries.sort(key = lambda x: x[2])
        i = 0
        solution = [True]*len(queries)
        
        for node1, node2, weight in queries:
            query = (node1, node2, weight)
            while i< len(edgeList) and edgeList[i][2] < weight:
                a, b = edgeList[i][0], edgeList[i][1]
                union(a, b) 
                i += 1
            solution[indices[query]] = (isConnected(node1, node2))

        return solution
            
            