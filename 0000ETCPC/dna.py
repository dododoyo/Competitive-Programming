for _ in range(int(input())):
  dna1,dna2 = input().split()
  solution = 0
  for  i in range(len(dna1)):
    solution += (dna1[i] != dna2[i])
  print(solution)
