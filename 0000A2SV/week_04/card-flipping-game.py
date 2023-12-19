class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalidNumbers = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                invalidNumbers.add(fronts[i])
        solution = float('inf')
        for number in (fronts+backs):
            if number not in invalidNumbers:
                solution = min(solution,number)
        return solution if solution != float('inf') else 0

        