# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edge = [[] for i in range(len(points))]
        heap = [(0, 0)]
        visited = set() 
        
        for point in range(len(points)):
            for neigh in range(point + 1, len(points)):
                manhattan = abs(points[point][0] - points[neigh][0]) + abs(points[point][1] - points[neigh][1])
                edge[point].append((neigh, manhattan))
                edge[neigh].append((point, manhattan))
        
        solution = 0
        while len(visited) < len(points):
            cost, curr = heappop(heap)
            if curr in visited:
                continue
            solution += cost

            for neigh in edge[curr]:
                heappush(heap, (neigh[1], neigh[0]))
            
            visited.add(curr)
        return solution
            