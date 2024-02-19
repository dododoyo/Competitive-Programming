for _ in range(int(input())):
  n = int(input())
  ones_counter = [0]*n
  for j in range(n):
    row,ones = input(),0
    for i in range(n):
      ones += row[i] == "1"
    ones_counter[j] = ones
  for k in range(1,n):
    # check for squares
    if ones_counter[k] == ones_counter[k-1] and ones_counter[k] != 0:
      print("SQUARE")
      break
    # check for triangles
    if abs(ones_counter[k] - ones_counter[k-1]) == 2 and ones_counter[k]%2 and ones_counter[k-1]%2:
      print("TRIANGLE")
      break
