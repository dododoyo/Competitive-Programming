# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

from bisect import bisect_left
for _ in range(int(input())):
  n = int(input())
  tracks = list(map(int, input().split()))
  queries = int(input())

  tracks_prefix = [0]*(n+1)
  for i in range(n):
    tracks_prefix[i+1] = tracks[i] + tracks_prefix[i]

  # the sum of length of sections/(not arr[i]) between 
  # left to right must be less than or equal to "u"
  # find r !
  for i in range(queries):
    left,power = map(int,input().split())
    right,temp = left,0
    max_reach = power+tracks_prefix[left-1]

    # x = valid_track(tracks_prefix,max_reach)
    x = bisect_left(tracks_prefix,max_reach)
    for j in range(max(left, x-3), min(x+3, n+1)):
      y = tracks_prefix[j] - tracks_prefix[left-1]

      if temp < power*y - y*(y-1)//2:
        temp = power*y - y*(y-1)//2
        right = j

    print(right,end = " ")
  print()