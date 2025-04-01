from sys import stdin
def input(): return stdin.readline().strip()

# check if the sum of array is perfect square 
def find_sqrt(num):
  left,right = 1,num 
  solution = 1

  while left <= right:
    middle = left + (right-left)//2
    squared = middle*middle

    if squared == num:
      return middle
    elif squared > num:
      right = middle - 1
    else:
      solution = left
      left = middle + 1
  return solution


for _ in range([int(i) for i in input().split()][0]):
  buckets = [int(i) for i in input().split()][0]
  squares = [int(i) for i in input().split()]


  total_squares = sum(squares)

  sqt = find_sqrt(total_squares)

  if sqt*sqt == total_squares:
    print("YES")
  else:
    print("NO")