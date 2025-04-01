from sys import stdin
def input(): return stdin.readline().strip()

m,n = [int(i) for i in input().split()]
data = [[int(i) for i in input().split()] for _ in range(n)]

def is_good(time):
    total = 0
    for i in range(n):
        temp_time = time
        t,z,rest = data[i]
        curr_ballons = 0

        if temp_time // t > z:
            time_to_fill_z_ballons = t*z + rest

            curr_ballons = z * (temp_time//time_to_fill_z_ballons)
            left_time = temp_time % (time_to_fill_z_ballons)

            # if the assistant will have time to rest 
            # one more time
            if left_time // t > z:
                curr_ballons += z
            else:
                curr_ballons += (left_time // t)
                
        # only one round and can't fill 
        # more than z number of ballons
        else:
            curr_ballons = temp_time // t

        total += curr_ballons
    
    return total >= m

def find_arr(time):
    solution = [0] * n
    
    for i in range(n):
        temp_time = time
        t,z,rest = data[i]

        if temp_time // t > z:
            time_to_fill_z_ballons = t*z + rest
            total_rests = (temp_time//time_to_fill_z_ballons)

            solution[i] = z * total_rests

            left_time = temp_time % (time_to_fill_z_ballons)

            # if the assistant will have time to rest 
            # one more time
            if left_time // t > z:
                solution[i] += z
            else:
                solution[i] += (left_time // t)

        # only one round and can't fill 
        # more than z number of ballons
        else:
            solution[i] = temp_time // t
    
    return solution

if m == 0:
  print(0)
  print(*[0 for _ in range(n)])
else:
  low, high= 0, int(1e9)
  valid = high

  while low <= high:

    mid = (low + high) // 2

    if is_good(mid):
        valid = mid
        high = mid - 1
    else:
        low = mid + 1

  solution = find_arr(valid)
  print(valid)

  res = [0]*n
  curr = m

  for i in range(n):
    if solution[i] > curr:
        res[i] = curr
    else:
        res[i] = solution[i]

    curr -= solution[i]

    if curr < 0:
        break
    
  print(*res)