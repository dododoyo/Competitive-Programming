# it's sorted 
# from in to out 
# from out to in

already_sorted = True
n = int(input())
nums = list(map(int,input().split()))
if n < 4:
  print("no")
  exit(0)

for i in range(1,n):
  if nums[i] < nums[i-1]:
    already_sorted = False
    break


if already_sorted:
  print("no")
  exit(0)

reverse_sorted = True
for i in range(1, n):
  if nums[i] > nums[i-1]:
    reverse_sorted = False
    break

if reverse_sorted:
  print("no")
  exit(0)

odds_increasing = True
for i in range(1,n,2):
  if nums[i] < nums[i-2]:
    odds_increasing = False
    break

odds_decreasing = True
for i in range(3,n,2):
  if nums[i] > nums[i-2]:
    odds_decreasing = False
    break

evens_increasing = True
for i in range(2,n,2):
  if nums[i] < nums[i-2]:
    evens_increasing = False
    break

evens_decreasing = True
for i in range(2,n,2):
  if nums[i] > nums[i-2]:
    evens_decreasing = False
    break

if (evens_decreasing and odds_increasing) or (odds_decreasing and evens_increasing):
  print("no")
else:
  print('yes')