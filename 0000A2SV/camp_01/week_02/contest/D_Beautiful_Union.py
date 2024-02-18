from collections import defaultdict
def solver(a,b):
  # using two pointers won't work
  # use counter to count 
  a_counter, b_counter = defaultdict(int), defaultdict(int)
  curr_freq, prev_num = 0, a[0]
  for number in a:
    if number == prev_num:
      curr_freq += 1
    else:
      curr_freq = 1
      prev_num = number
    a_counter[number] = max(curr_freq, a_counter[number]) 

  curr_freq, prev_num = 0, b[0]
  for number in b:
    if number == prev_num:
      curr_freq += 1
    else:
      curr_freq = 1
      prev_num = number
    b_counter[number] = max(curr_freq, b_counter[number]) 

  max_len = 0
  for a_key in a_counter.keys():
    max_len = max(max_len,a_counter[a_key]+b_counter[a_key])
  for b_key in b_counter.keys():
    max_len = max(max_len,a_counter[b_key]+b_counter[b_key])

  return max_len



for _ in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  print(solver(a,b))