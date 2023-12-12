n = int(input())
#this is a math question 
#for k as an input we have a sequence of i*(n-i)+1 i from 1 upto k we have to sum these terms
k = n
sum_ = 0
for i in range(1,n+1):
    sum_ += i*(k-i) +1
print(sum_)
