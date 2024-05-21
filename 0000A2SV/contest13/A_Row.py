n = int(input())
seats = input()

if (n == 1 and seats[0] == "0") or (n > 1 and seats[:2] == "00"):
  print("No")
  exit(0)

if (n > 2 and (seats[n-3:] == "100" or n > 2 and seats[:3] == "001")):
    print("No")
    exit(0)

for i in range(1,n):
  if (seats[i-1:i+1] ==  "11") or (i < n-1 and  seats[i-1:i+2] == "000"):
    print("No")
    exit(0)
print("Yes")