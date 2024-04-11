# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":return 0
        if "0000" in deadends:return -1

        deadends = set(deadends)
        current_level,level,visited = ["0000"],1,{"0000"}
    
        def possiblePaths(node):
            paths = []
            for index,val in [[0,1],[0,-1],[1,1],[1,-1],[2,1],[2,-1],[3,1],[3,-1]]:
                path = list(node)
                path[index] = str((int(path[index]) + val + 10)%10)
                paths.append("".join(path))
            return paths

        while current_level:
            next_level = []
            for node in current_level:
                for path in possiblePaths(node):
                    if path == target:
                        return level
                    if path not in deadends and path not in visited:
                        next_level.append(path)
                        visited.add(path)
            current_level = next_level
            level += 1
        return -1