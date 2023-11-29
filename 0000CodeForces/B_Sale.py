#use sliding window of static size to find max sum
n,m = map(int,input().split())
money = list(map(int,input().split()))

#code to open the first window
curr_sum = 0
l=0

while l < m:
    curr_sum += money[l];l+=1

max_sum = curr_sum
print(max_sum)
r = 1
while l < n:
    curr_sum = money[l] - money[r-1]
    max_sum = max(max_sum,curr_sum)
    l+=1;r+=1
print(max_sum)
