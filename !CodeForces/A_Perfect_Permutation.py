n = int(input())
sol = [""]*(n)
if n == 1:
    print('-1')
    exit()
sol[-1] = "1"
for i in range(n-1):
    sol[i] = str(i+2)

print(" ".join(sol))