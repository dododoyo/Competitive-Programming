n,d = map(int,input().split())
songs = [int(i) for i in input().split()]

all_time = sum(songs)
performance = all_time + (n-1)*10 
if performance > d:
  print(-1);exit(0);

devu = (n-1)*2 + ((d-performance)//5)

print(devu)