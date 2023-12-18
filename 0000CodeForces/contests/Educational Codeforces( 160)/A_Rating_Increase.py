for _ in range(int(input())):
  s = input()
  found = False
  for i in range(1, len(s)):
    a, b = s[:i], s[i:]
    if b[0] != '0' and int(b) > int(a):
      print(a, b)
      found = True
      break
  if not found:
    print(-1)