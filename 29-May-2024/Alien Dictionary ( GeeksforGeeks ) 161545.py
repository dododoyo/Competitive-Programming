# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = [[] for _ in range(K)]
        indegree = [0]*K
        
        for i in range(N-1):
            j = i+1
            
            current = alien_dict[i]
            checked = alien_dict[j]
            
            p1,p2 = 0,0
            
            while p1 < len(current) and p2 < len(checked) and current[p1] == checked[p2]:
                p1,p2 = p1+1,p2+1
                
            if p1 < len(current) and p2 < len(checked):
                graph[ord(current[p1])-97].append(ord(checked[p2])-97)
                indegree[ord(checked[p2])-97] += 1
    
        bfs_que = [node for node in range(K) if not indegree[node]]
        solution = []
        
        while bfs_que:
            solution.extend(bfs_que)
            next_que = []
            
            for node in bfs_que:
                for neighbor in graph[node]:

                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        next_que.append(neighbor)
            bfs_que = next_que[:]
        
        return [chr(i+97) for i in solution]
               