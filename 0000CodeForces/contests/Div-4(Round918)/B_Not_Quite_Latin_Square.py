for _ in range(int(input())):
  matrix = []
  for i in range(3):
    row = list(input())
    matrix.append(row)
  a,b,c = False,False,False
  for i in range(3):
    if "?" in matrix[i]:
      for k in matrix[i]:
        if k == "A":
          a = True
        elif k == "B":
          b = True
        elif k == "C":
          c = True

  if not a:print("A")
  if not b:print("B")
  if not c:print("C")
      
    