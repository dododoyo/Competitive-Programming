for _ in range(int(input())):
  s = input()
  allSame = True
  n = len(s)
  for i in range(1,n):
    if s[i] != s[i-1]:
      allSame = False
      break
  if allSame:
    print(-1)
  else:
    print(n-1)