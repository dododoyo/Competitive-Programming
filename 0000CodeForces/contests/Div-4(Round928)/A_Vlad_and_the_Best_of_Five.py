for _ in range(int(input())):
  s = input()
  A = B= 0
  for i in s:
    A += i=="A"
    B += i=="B"
  if A > B:print("A")
  else:print("B")