from collections import defaultdict
"""
given an array of integers 
return the sub-array left,right 
such that right-left-num_of_distinct_colors is maximized

right should be maximum 
left should be minimum
distinct should also be minimum

we want to get a window where our elements are more repeated

repeated elements maximize  our window size

Choose 2 integers l and r such that l≤r and r-l-c(l,r) is maximized."""

for _ in range(int(input())):
  n = int(input())
  colors = input()
  print(1,n)