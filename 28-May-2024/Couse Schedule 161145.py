# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, relations: List[List[int]]) -> bool:
        pre_requisites = [[] for _ in range(numCourses)]
        indegrees = [0]*numCourses

        for relation in relations:
            course,pre = relation
            pre_requisites[course].append(pre)

        for relation in relations:
            indegrees[relation[1]] += 1
        
        bfs_que = [node for node in range(numCourses) if indegrees[node] == 0]
        courseCounter = 0

        while bfs_que:
            next_que  = []
            courseCounter += len(bfs_que)
            for node in bfs_que:
                for neighbor in pre_requisites[node]:
                    indegrees[neighbor] -= 1

                    if indegrees[neighbor] == 0:
                        next_que.append(neighbor)
            bfs_que = next_que[:]

        return courseCounter == numCourses