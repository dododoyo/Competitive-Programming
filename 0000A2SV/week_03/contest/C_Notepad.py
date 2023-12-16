for _ in range(int(input())):
    n = int(input())
    x = input()
    for i in range(n - 2):
        s = x[i]+x[i+1]
        # print(s)
        if x.count(s)>1:
            print("YES")
            break
    else:print("NO")