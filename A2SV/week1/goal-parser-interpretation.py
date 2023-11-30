class Solution:
    def interpret(self, command: str) -> str:
        solution = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                solution.append("G")
                i+=1
            elif command[i] == "(":
                if command[i+1] == ")":
                    solution.append("o")
                    i+=2
                else:
                    solution.append("al")
                    i+=4
        return "".join(solution)