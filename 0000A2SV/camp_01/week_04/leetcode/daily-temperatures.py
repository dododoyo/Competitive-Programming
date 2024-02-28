class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        solution = [0]*len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                cur = stack.pop()
                # whomever popped it is greater than it
                solution[cur] = i - cur
            stack.append(i)
        return solution