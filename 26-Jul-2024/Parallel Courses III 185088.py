# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = {i:0 for i in range(1,n+1)}
        for x,y in relations:
            graph[x].append(y)
            indegree[y]+=1

        solution = 0
        q = deque([[i,time[i-1]] for i in indegree if indegree[i]==0])
        time_dict = {i:time[i-1] for i in range(1,n+1)}

        while q:
            num,month = q.popleft()
            solution = max(time_dict[num],solution)
            for neighbor in graph[num]:
                indegree[neighbor]-=1

                if time_dict[neighbor]<month+time[neighbor-1]:
                    time_dict[neighbor]=month+time[neighbor-1]

                if indegree[neighbor]==0:
                    q.append([neighbor,time_dict[neighbor]])
        return solution
            

