"""
If both groups contribute equally let's add them 
then sort them 
Sort both arrays using the their sum in reverse order
odd elements for anatoli 
evens for bisrat    #score = anatoli_sum - bisrat_sum
"""
for _ in range(int(input())):
  n = int(input())
  anatoli = list(map(int,input().split()))
  bisrat = list(map(int,input().split()))
  sum_array = [[anatoli[i]+bisrat[i],anatoli[i],bisrat[i]] for i in range(n)]
  sum_array.sort(reverse=True)
  anatoli_sum,bisrat_sum = 0,0
  for i in range(n):
    if i%2:# bisrat's turn 
      bisrat_sum += sum_array[i][2] - 1
    else:# anatoli's turn
      anatoli_sum += sum_array[i][1] - 1
  print(anatoli_sum - bisrat_sum)