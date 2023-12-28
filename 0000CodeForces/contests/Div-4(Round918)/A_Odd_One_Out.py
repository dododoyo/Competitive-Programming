from collections import Counter
for _ in range(int(input())):
  abc = list(map(int,input().split()))
  a = ""
  count = Counter(abc)
  for i in count.keys():
    if count[i] == 1:
      print(i)
