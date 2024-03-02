k = int(input())
l = int(input())
importance = [0]
def is_power(k,l):
  if l == 1:return True
  if l%k:return False
  importance[0] += 1
  return is_power(k,l//k)

if is_power(k,l):
  print("YES\n", importance[0]-1)
else:
  print("NO")