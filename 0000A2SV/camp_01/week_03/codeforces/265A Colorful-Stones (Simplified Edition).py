s = input()
t = input()
current_stand = 0
for i in range(len(t)):
  if s[current_stand] == t[i]:
    current_stand += 1
print(current_stand+1)