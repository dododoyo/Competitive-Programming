for _ in range(int(input())):
  n = int(input())
  a = [int(num) for num in input().split()]
  s = input()
  queries = int(input())

  pref = [0] * (n + 1)
  for i in range(1, n + 1):
    pref[i] = pref[i - 1] ^ a[i-1]

  x0 = 0
  x1 = 0
  for i in range(n):
    if s[i] == "0":
      x0 ^= a[i]
    else:
      x1 ^= a[i]

  for i in range(queries):
      query = [int(num) for num in input().split()]
      if query[0] == 2:
        if query[1]:
          print(x1,end=" ")
        else:
          print(x0,end=" ")
      else:
        l, r = query[1], query[2]
        seg = pref[r] ^ pref[l - 1]
        x0 ^= seg
        x1 ^= seg
  print()