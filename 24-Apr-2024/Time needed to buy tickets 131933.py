# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        current, solution = 0, 0
        
        # simulate the process until you get the answer
        while True:
            if tickets[current]:
                tickets[current] -= 1
                solution += 1

            if current == k and tickets[current] == 0:
                return solution

            current += 1
            
            # start the loop again
            if current == len(tickets):
                current = 0
