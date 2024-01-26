n = int(input())
found_answer = False
price_quality = []
for _ in range(n):
  # a == price ,, b == quality
  price_quality.append(list(map(int,input().split())))
# print(price_quality)
price_quality.sort()

for right in range(n-1):
  if not found_answer:
    laptop1 = price_quality[right]
    laptop2 = price_quality[right+1]
    if laptop1[0] < laptop2[0] and laptop1[1] > laptop2[1]:
      print("Happy Alex")
      found_answer = True

if not found_answer:
  print("Poor Alex")

