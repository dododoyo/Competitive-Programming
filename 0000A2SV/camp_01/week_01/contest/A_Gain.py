for _ in range(int(input())):
  n = int(input())
  strengths = [int(i) for i in input().split()]
  largest_till_now = [strengths[0]]*n
  largest_after_now = [strengths[-1]]*n
  max_forward,max_backward = strengths[0],strengths[-1]
  for i in range(1,n):
    max_forward = max(max_forward,strengths[i])
    max_backward = max(max_backward,strengths[n-i-1])
    largest_after_now[n-i-1] = max_backward
    largest_till_now[i] = max_forward
  
  solution = [0]*n
  for i in range(n):
    if i == 0:
      solution[i] = strengths[i] - largest_after_now[1]
    elif i == n-1:
      solution[i] = strengths[i] - largest_till_now[-2]
    else:
      if largest_till_now[i-1] > largest_after_now[i+1]:
        solution[i] = strengths[i] - largest_till_now[i-1]
      else:
        solution[i] = strengths[i] - largest_after_now[i+1]
  print(*solution)