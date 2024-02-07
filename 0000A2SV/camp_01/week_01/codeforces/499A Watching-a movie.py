n,x = map(int,input().split())
minutes_watched = 0

#`current_minute` is initialized to 1 because the problem statement
# mentions that the movie is initially turned on at the first minute. 
current_minute = 1
"""
The solution is calculated as the sum of the number 
of minutes to skip to reach the start of each best moments
and the duration of the best moments. 

The number of minutes to skip is calculated as 
(start - current_minute) % x
"""
for _ in range(n):
  best_start,best_end = map(int,input().split())
  minutes_till_best = (best_start - current_minute) % x
  best_duration = (best_end-best_start+1)
  minutes_watched += (minutes_till_best + best_duration)
  current_minute = best_end+1

print(minutes_watched)

