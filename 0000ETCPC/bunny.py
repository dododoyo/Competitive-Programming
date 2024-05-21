rows,column,k = map(int,input().split())
for i in range(rows):
  row = input()
  amplified_row = [j*k for j in row]
  for g in range(k):
    print("".join(amplified_row))
