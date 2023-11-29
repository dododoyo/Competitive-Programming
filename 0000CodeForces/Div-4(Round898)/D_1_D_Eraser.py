def minOperation(n,k,string):
  counter = 0
  l,r = 0,0;
  while r < n:
    if string[r] == 'W':
      r += 1

    else:
      l = r;
      while r < n and r-l < k:
        r += 1
        # print(r);
      l = r
      counter +=1
  return counter;

t = int(input());
for _ in range(t):
  n,k = map(int,input().split());
  string = input();
  print(minOperation(n,k,string));


