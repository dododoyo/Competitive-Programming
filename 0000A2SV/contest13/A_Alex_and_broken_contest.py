freinds = ["Danil", "Olya", "Slava", "Ann","Nikita"]
s = input()

in_contest = 0

for i in range(len(s)-6+1):
  if s[i:i+6] == "Nikita":
    in_contest += 1

for i in range(len(s)-5+1):
  if s[i:i+5] == "Danil" or s[i:i+5] == "Slava":
    in_contest += 1

for i in range(len(s)-3+1):
  if s[i:i+3] == "Ann":
    in_contest += 1

for i in range(len(s)-4+1):
  if s[i:i+4] == "Olya":
    in_contest += 1

if in_contest == 1:
  print("YES")
else:
  print("NO")
