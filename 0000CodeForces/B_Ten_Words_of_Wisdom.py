for _ in range(int(input())):
  n = int(input())
  solution = [0,0]
  for i in range(n):
    words, quality = map(int, input().split())
    if words < 11 and quality > solution[1]:
        solution = [i,quality]
  print(solution[0]+1)