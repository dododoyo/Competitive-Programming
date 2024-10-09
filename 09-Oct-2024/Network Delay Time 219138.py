# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)   
        for source, target, cost in times:
            graph[source].append((target, cost))
        
        cost = [float('inf') for i in range(N)]
        cost[K-1] = 0
        
        pq = PriorityQueue()
        pq.put((0, K))
        
        while not pq.empty():
            curr_cost, curr_node = pq.get()
            
            for neighbor, weight in graph[curr_node]:
                if curr_cost+weight<cost[neighbor-1]:
                    cost[neighbor-1] = curr_cost+weight
                    pq.put((cost[neighbor-1], neighbor))
        
        ans = max(cost)
        return ans if ans!=float('inf') else -1