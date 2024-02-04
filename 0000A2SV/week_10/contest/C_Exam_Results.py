n = int(input())
result = [int(i) for i in input().split()]

result.sort()

solution = [result[0]]*n
sorted_happy_count = 0
for i in range(1,n-1):
    sorted_happy_count +=result[i] < result[i+1]



left ,right = 1,n-1
i = 1

while left < right:
  solution[i] = result[left]
  solution[i+1] = result[right]
  i += 2
  left,right = left+1,right-1

  # print(solution)

shuffled_happy_count = 0
for i in range(1,n-1):
    shuffled_happy_count += solution[i] < solution[i+1]

if shuffled_happy_count > sorted_happy_count:
   print(shuffled_happy_count)
else:
   print(sorted_happy_count)