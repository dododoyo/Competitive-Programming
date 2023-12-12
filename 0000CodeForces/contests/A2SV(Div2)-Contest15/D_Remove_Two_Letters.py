def diff_string(n,s):
  sol = n - 1
  for i in range(1,n-1):
      if s[i-1] == s[i+1]:
          sol -= 1
  return sol

for _ in range(int(input())):
  n = int(input());
  s = input();
  print(diff_string(n,s));
