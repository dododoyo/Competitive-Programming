for _ in range(int(input())):
  racers = list(map(int,input().split()))
  counter = 0
  for i in range(1,4):
    if racers[i] > racers[0]:
      counter+=1
  print(counter)
