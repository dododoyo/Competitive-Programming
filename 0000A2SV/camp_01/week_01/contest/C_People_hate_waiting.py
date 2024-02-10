n = int(input()) # people in the queue
queue_line = list(map(int,input().split()))
queue_line.sort()
waiting_time,accumulator = [0]*(n),0

for i in range(n):
  waiting_time[i] = accumulator
  if accumulator <= queue_line[i]:
    accumulator += queue_line[i]

disappointed = 0
for i in range(n):
  if waiting_time[i] > queue_line[i]:
    disappointed += 1
print(n-disappointed)