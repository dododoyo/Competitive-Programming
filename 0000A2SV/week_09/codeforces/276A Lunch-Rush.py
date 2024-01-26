# n == number of restaurants available
# k == time given for a lunch break

# ti = time passed eating in ith restaurant 

#fi = satisfaction from dining in i'th restaurant provided it came on time  

n,k = map(int,input().split())
max_joy = -float("inf")
for i in range(n):
  f,t= map(int,input().split())
  joy = 0
  if t > k:joy = f - t + k
  else:joy = f
  max_joy = max(max_joy,joy)
print(max_joy)