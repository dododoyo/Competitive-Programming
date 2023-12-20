for _ in range(int(input())):
  n = int(input())
  log = input()
  minute_counter,offset = [0]*26,ord("A")
  for problem in log:
    minute_counter[ord(problem)-offset] += 1
  solved_problems = [True for i in range(26) if minute_counter[i] > i ]
  print(sum(solved_problems))