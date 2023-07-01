class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        solution=[]
        for i in asteroids:
            while len(solution) > 0 and i < 0 and solution[-1] > 0:
                if i+solution[-1] > 0:i=0;
                elif i+solution[-1] <0:solution.pop();
                else:i=0;solution.pop();
            if i:solution.append(i);
        return solution;