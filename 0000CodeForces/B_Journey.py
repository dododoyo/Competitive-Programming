from sys import stdin
def input(): return stdin.readline().strip()


# find the first position 
# where sum will pass or equal to n 

for _ in range([int(i) for i in input().split()][0]):
  kilometers,a,b,c = [int(i) for i in input().split()]
  left_over = {0:0,1:a,2:a+b}

  left,right = 1,kilometers
  solution = kilometers

  while left <= right:
    middle = left + (right-left)//2

    middle_distance = (middle//3) * (a+b+c)
    middle_distance += left_over[middle%3]
    
    if middle_distance >= kilometers:
      solution = middle 
      right = middle - 1
    else:
      left = middle + 1

  print(solution)