# x^y > 0 means y can't be x
# x&y > 0 => solution must have bit set at least significant bit

for _ in range(int(input())):
  n = int(input())
  if n == 1:
    print(3)
    continue
  # get the position of least significant bit.
  least_position = 0
  for i in range(256):
    if 1<<i & n != 0:
      least_position = i
      break
  solution = 1 << least_position
  solution += (solution == n)
  print(solution)