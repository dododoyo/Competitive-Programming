# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = [[] for course in range(numCourses)]

        for course,pre_req in prerequisites:
            preMap[course].append(pre_req)

        visited,cycle,solution = set(),set(),[]

        def dfs(course):
            if course in cycle:return False
            if course in visited:return True

            cycle.add(course)
            for pre_req in preMap[course]:
                if dfs(pre_req) == False:return False
                
            cycle.remove(course)
            visited.add(course)
            solution.append(course)

            return True
        for course in range(numCourses):
            if not dfs(course):
                return []

        return solution