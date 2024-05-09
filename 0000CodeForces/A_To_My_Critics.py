for _ in range(int(input())):
  a,b,c = map(int,input().split())
  possibles = [a+b,b+c,a+c]
  print("YES" if max(possibles) >= 10 else "NO")