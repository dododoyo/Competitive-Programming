from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]


def encode(number):
  solution = []
  while number:
    solution.append(str(number%3))
    number //= 3

  return "".join(reversed(solution))

def decode(number):
  solution = 0
  p = 0
  for i in range(len(number)-1,-1,-1):
    # print(number[i] * (3**(p)))
    solution += number[i] * (3**p)
    p += 1
  return solution

num1,num2 = ls()
# convert to ternary 
t1 = encode(num1)
t2 = encode(num2)


n1,n2 = len(t1),len(t2)
if n1 < n2:
  t1 = "0"*(n2-n1) + t1
else:
  t2 = "0"*(n1-n2) + t2
# print(t1)
# print(t2)

solution = ["0"]*len(t1)

for i in range(len(t1)):
  if t1[i] == t2[i]:
    solution[i] = 0
  elif [t1[i],t2[i]] in [["0","1"],['1','2'],['2','0']]:
    solution[i] = 1
  else:
    solution[i] = 2
  # print(int(t1[i]),int(t2[i]),solution[i])

# print(solution)
print(decode(solution))