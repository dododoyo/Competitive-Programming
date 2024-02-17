class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits,solution = {},0
        for answer in answers:
            if answer == 0:
                solution += 1
            elif answer not in rabbits:
                rabbits[answer] = 1
            else:
                rabbits[answer] += 1
                if rabbits[answer] == answer + 1:
                    solution += answer + 1
                    rabbits[answer] = 0
        
        for key in rabbits:
            if rabbits[key] > 0:
                solution += key + 1
        return solution