#Not Solved
num = input()
one_counter = 0
four_counter = 0
sol,i = 'YES',0
while i < len(num)-3 :
    if num[i] == '1' and num[i+1] == '4' and num[i+2] == '4':i+=3
    elif num[i] == '1' and num[i+1] == '4':i+=1
    elif num[i] == '1':i+=1
    else:sol='NO';break
while i < len(num)-2 :
    if num[i] == '1' and num[i+1] == '4':i+=1
    elif num[i] == '1':i+=1
    else:sol='NO';break
while i < len(num) :
    if num[i] == '1':i+=1
    else:sol='NO';break

print(sol)