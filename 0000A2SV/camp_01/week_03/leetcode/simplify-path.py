class Solution:
    def simplifyPath(self, path: str) -> str:
        solution = []
        commands = path.split("/")
        for command in commands:
            if command == "..":
                # popping and element means going back in directory
                if solution:
                    solution.pop()
            elif command not in ("","."):
                # command is  a word
                solution.append(command)
        return "/" + "/".join(solution)
        