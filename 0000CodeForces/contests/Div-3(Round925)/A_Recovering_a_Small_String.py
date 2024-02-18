for _ in range(int(input())):
  n = int(input())
  offset = ord("a")-1
  a,b,c = 1,1,1
  if n < 29:
    c = n-2
  elif n > 28 and n < 53:
    c = 26
    b = n-27
  else:
    c = 26
    b = 26
    a = n - 52
  # print(a,b,c)
  a,b,c = chr(a+offset),chr(b+offset),chr(c+offset)
  print(a+b+c)
