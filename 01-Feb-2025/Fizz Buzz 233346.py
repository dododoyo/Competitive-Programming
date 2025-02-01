# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, i: int) -> List[str]:
        solution = []
        for n in range(1,i+1):
            if n % 15 == 0:
                solution.append("FizzBuzz")
            elif n % 3 == 0:
                solution.append("Fizz")
            elif n % 5 == 0:
                solution.append("Buzz")
            else:
                solution.append(str(n))

        return solution