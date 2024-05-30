# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # use  a form of dp to store all the course grand-pres and pres
        curriculum = defaultdict(list)
        for pre_req,course in prerequisites:
            curriculum[course].append(pre_req)
        
        preMap = {}

        def dfs(course):
            # no pres
            if course not in preMap:
                preMap[course] = {course}
                for neighbor in curriculum[course]:
                    neighbor_pres = dfs(neighbor)
                    preMap[course] |= neighbor_pres
            return preMap[course]

        # populate the preMap with the courses
        for course in range(numCourses):
            dfs(course)
        n = len(queries)
        solution = [False]*n

        for i in range(n):
            course,pre = queries[i]
            solution[i] = course in preMap[pre]
        return solution
        

