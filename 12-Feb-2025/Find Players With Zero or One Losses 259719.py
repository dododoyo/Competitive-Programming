# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # key=player_id | val=[wins,loses]
        match_scores = defaultdict(lambda: [0,0])
        # for each team count 
        # how many times they won 
        # and how many times they lost 

        for winner,loser in matches:
            match_scores[winner][0] += 1
            match_scores[loser][1] += 1

        players = match_scores.keys()

        solution = [[],[]]
        for player in players:
            wins,loses = match_scores[player]

            if loses == 0:
                solution[0].append(player)
            elif loses == 1:
                solution[1].append(player)

        solution[0].sort()
        solution[1].sort()
        
        return solution