#given three strings 
t = int(input())
for _ in range(t):
    a = input()
    b = input()
    c = input()
    n,op = len(c), 0


    for i in range(n):
        if b[i] != c[i] and a[i] == c[i]:
            b = b[:i] + c[i] + b[i+1:]
            op +=1
        elif a[i] != c[i] and b[i] == c[i]:
            a = a[:i] + c[i] + a[i+1:]
            op += 1
        elif a[i] == b[i] and b[i] == c[i]:
            op += 1
    # if the number of swaps performed is equal to the length 
    # of the strings (n), it means all characters in string c
    # have been swapped successfully
    if n == op:
        print("YES")
    else:
        print("NO")