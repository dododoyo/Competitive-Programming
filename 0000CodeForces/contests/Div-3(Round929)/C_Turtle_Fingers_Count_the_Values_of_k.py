for _  in range(int(input())):
  a,b,l = map(int, input().split())
  seen = set()
  solution = 0
  # brute force
  for i in range(20):
    for j in range(20):
      k = l //((a**i) * (b**j))
      remain = l  % ((a**i) * (b**j))
      
      if remain  == 0  and k not in seen:
        solution += 1
        seen.add(k)
  print(len(seen))
