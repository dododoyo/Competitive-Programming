# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def isNotBipartite(self,node):
        dq = deque()

        dq.append(node)
        self.colors[node] = 1

        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()

                for nghbr in self.graph[node]:
                    if self.colors[nghbr] == self.colors[node]:
                        return True

                    if self.colors[nghbr] == -1:
                        self.colors[nghbr] = 1 - self.colors[node]
                        dq.append(nghbr)

        return False
        

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # construct the graph 
        self.graph = [[] for _ in range(n)]
        self.colors = [-1]*n

        for a,b in dislikes:
            self.graph[a-1].append(b-1)
            self.graph[b-1].append(a-1)

        
        # see if it can be 
        # colored black and white
        # use bfs 
        for i in range(n):
            if self.colors[i] == -1 and self.isNotBipartite(i):
                    return False 

        return True