n = int(input())
strings = [input() for _ in range(n)]
strings.sort(key = lambda x:len(x))
for i in range(1,n):
  if strings[i-1] not in strings[i]:
    print("NO")
    exit(0)
print("YES")
for string in strings:
  print(string)