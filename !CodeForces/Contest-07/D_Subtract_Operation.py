def find_k():
    n,k = map(int,input().split())
    the_list = set(map(int, input().split()))
    for i in the_list:
        if i+k in the_list:print('YES');break;
    else:print('NO')
    
for _ in range(int(input())):
    find_k()