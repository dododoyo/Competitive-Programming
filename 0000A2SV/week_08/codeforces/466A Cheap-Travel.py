n,m,a,b = map(int,input().split())
# n == total number of rides
# m == rides per special ticket
# a == normal ticket price
# b == special ticket price

normal_price = n*a
special_tickets = n//m

if n%m:
  special_price = special_tickets*b + (n%m)*a
else:
  special_price = special_tickets*b

all_special = (n//m + 1)*b
print(min(normal_price,special_price,all_special))