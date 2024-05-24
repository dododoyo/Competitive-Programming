t = int(input())
for _ in range(t):
  n= int(input())
  original = input()

  r = sorted(list(set(original)))

  encoder = {}
  f = 0
  b = len(r) - 1
  while f <= b:
    encoder[r[f]] = r[b]
    encoder[r[b]] = r[f]
    f += 1
    b -= 1
  ans = []
  for i in range(n):
    ans.append(encoder[original[i]])
  print("".join(ans))
  


