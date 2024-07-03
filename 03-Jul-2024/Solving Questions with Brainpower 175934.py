# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

from collections import defaultdict
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp  = defaultdict(lambda : -1)
        
        def find_max(current_index):
            if current_index > n-1:
                return 0

            if current_index == n - 1:
                return questions[current_index][0]
            not_pick,next_value = 0,0
            if dp[current_index+1] == -1:
                not_pick = find_max(current_index+1)
            else:
                not_pick = dp[current_index+1]


            if dp[current_index+1+questions[current_index][1]] == -1 :
                next_value = find_max(current_index+1+questions[current_index][1])
            else:
                next_value = dp[current_index+1+questions[current_index][1]]


            pick = questions[current_index][0] + next_value

            dp[current_index] = max(pick,not_pick)

            return dp[current_index]
            
        return find_max(0)