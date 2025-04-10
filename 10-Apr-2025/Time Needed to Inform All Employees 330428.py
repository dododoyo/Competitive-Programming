# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return informTime[0]

        tree = [[] for _ in range(n)]

        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        def dfs(node):
            if not tree[node]:
                return 0

            node_time = informTime[node]
            max_child = 0

            for child in tree[node]:
                max_child = max(max_child,dfs(child))


            return max_child + node_time

        return dfs(headID)
        