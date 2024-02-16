class Solution:
    def minOperations(self, logs: List[str]) -> int:
        solution = []
        # we have three options 
        for log in logs:
            if log == "../":
                if solution:
                    solution.pop()
            elif log != "./":solution.append(log)
            # print(solution)
        return len(solution)

        