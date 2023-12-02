n = int(input())
integers = list(map(int,input().split()))

even_sum = 0
evens = []
odds = []
integers.sort()
for integer in integers:
  if integer %2== 0:
    evens.append(integer);
  else:
    odds.append(integer);

even_sum = sum(evens)
running_sum = 0
even_running_sum = 0
for i in range(len(odds)-1,-1,-1):
  running_sum += odds[i]
  if running_sum %2 == 0:
    even_running_sum = running_sum


print(even_sum+even_running_sum)
