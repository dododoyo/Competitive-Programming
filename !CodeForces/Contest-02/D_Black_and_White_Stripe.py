test_cases = int(input())
counter = 1
for i in range(test_cases):
    counter += 1
    k_and_n = input().split()
    n,k= int(k_and_n[0]),int(k_and_n[1])
    stripe = input().rstrip()
    recolor = 0
    for i in range(k):
        if stripe[i] == 'W':
            recolor += 1
    i,j,current = 0,k,recolor
    while(j < len(stripe)):
        if stripe[i] == 'W' and stripe[j] == 'B':current-= 1
        elif stripe[i] == 'B' and stripe[j] == 'W':current += 1
        recolor = min(recolor,current)
        j += 1
        i += 1
    print(recolor)
