def find_smallest(n,k,s):
  if k % 2 == 0:
      return (''.join(sorted(s)))
  else:
      evens = sorted([s[i] for i in range(0, n, 2)])
      odds = sorted([s[i] for i in range(1, n, 2)])

      sol = []
      for i in range(n):
          if i%2==0:
              sol.append(evens[i//2])
          else:
              sol.append(odds[i//2])

      return ''.join(sol)




for _ in range(int(input())):
  n,k = map(int,input().split());
  s = input()
  print(find_smallest(n,k,s))

