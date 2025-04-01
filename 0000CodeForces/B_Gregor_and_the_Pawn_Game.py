for _ in range([int(i) for i in input().split()][0]):
  n = [int(i) for i in input().split()][0]
  enemy = list(input())
  gregor = list(input())
  MOVES = [-1,0,1]
  solution = [0]*n
  for i in range(n):
    if gregor[i] == "1":
      
      for dx in MOVES:
        x = i + dx 

        if -1 < x < n and solution[x] != 1:
          # enemy 
          if enemy[x] == "1" and dx != 0:
            solution[x] = 1
            break
          
          elif dx == 0 and enemy[x] == "0":
            solution[x] = 1
            break

  print(sum(solution))