n = int(input())
perform = list(map(int,input().split()))
min = max = perform[0]
solution = 0
'''The performer amazing if only if if goes down
below his minimum performance or above his max performance 
so when change of min and max occurs is the number
of time he was amazing'''
for i in perform:
    if i > max:max = i;solution += 1
    if i < min:min = i;solution += 1
print(solution)