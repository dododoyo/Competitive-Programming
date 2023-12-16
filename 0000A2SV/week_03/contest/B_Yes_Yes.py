for _ in range(int(input())):
  s = input()
  checked = "Yes"*(len(s)//3 + 2)
  print(["NO","YES"][s in checked])