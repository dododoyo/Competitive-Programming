n,x = int(input()),0
for i in range(n):
    each_op = input()
    if each_op[0] == '+':x+=1
    elif each_op[0] == 'X' and each_op[1] == '+':x+=1
    elif each_op[0] == 'X' and each_op[1] == '-':x-=1
    else:x-=1
print(x)

