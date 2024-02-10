n = int(input()) # people in the queue
serving_time = list(map(int,input().split()))
serving_time.sort()
waiting_time,running_sum = [0]*(n),0

for i in range(n):
  waiting_time[i] = running_sum
  if running_sum <= serving_time[i]:
    running_sum += serving_time[i]

disappointed = 0
for i in range(n):
  if waiting_time[i] > serving_time[i]:
    disappointed += 1
print(n-disappointed)