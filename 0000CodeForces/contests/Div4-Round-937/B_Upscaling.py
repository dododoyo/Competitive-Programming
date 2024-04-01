template1 = "##.."*60
template2 = "..##"*60
# print(template)

for _ in range(int(input())):
  n = int(input())
  n_2 = 2*n
  for i in range(n):
    if i%2:
      print(template2[:n_2])
      print(template2[:n_2])
    else:
      print(template1[:n_2])
      print(template1[:n_2])
      # index is even