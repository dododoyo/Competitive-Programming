# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = [[] for _ in range(numCourses)]
        indegrees = [0]*numCourses

        for relation in prerequisites:
            course,pre = relation
            preMap[course].append(pre)
            indegrees[pre] += 1
        
        bfs_que = [node for node in range(numCourses) if indegrees[node] == 0]
        solution = []

        while bfs_que:
            next_que = []
            solution.extend(bfs_que)

            for node in bfs_que:
                for neighbor in preMap[node]:
                    indegrees[neighbor] -= 1

                    if indegrees[neighbor] == 0:
                        next_que.append(neighbor)

            bfs_que = next_que[:]
        
        if len(solution) == numCourses:
            return solution[::-1]
        else:
            return []