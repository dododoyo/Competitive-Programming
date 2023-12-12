k,r = map(int,input().split())
#k is price of shovel
#r coin of value avalaibe
possiblePrice = 0
shovels = 0
while True:
    #solution is correct if remainder of our price is r , so we can add r and buy
    #or it is divisible by 10 and we don't need to use the r changes
    if ( possiblePrice!=0 and possiblePrice%10==0) or possiblePrice%10 == r:break
    possiblePrice += k
    shovels += 1
print(shovels)

