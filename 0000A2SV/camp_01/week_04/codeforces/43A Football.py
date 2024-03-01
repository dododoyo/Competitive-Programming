from collections import defaultdict
team_score = defaultdict(int)
for _ in range(int(input())):
  team_score[input()] += 1
max_score = 0
max_team = ""
for team,score in team_score.items():
  if score > max_score:
    max_score = score
    max_team = team
print(max_team)