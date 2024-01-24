n = int(input())
arr = [int(i) for i in input().split()]
negatives,positives,zeros = [],[],[]
for i in range(n):
  if arr[i] < 0:negatives.append(arr[i])
  elif arr[i] > 0:positives.append(arr[i])
  else:zeros.append(arr[i])

if not len(negatives)%2:
  last = negatives.pop()
  zeros.append(last)
  
if positives:
  print(len(negatives),*negatives)
  print(len(positives),*positives)
  print(len(zeros),*zeros)
else:
  print(len(negatives)-2,*negatives[2:])
  print(2,*negatives[:2])
  print(len(zeros),*zeros)