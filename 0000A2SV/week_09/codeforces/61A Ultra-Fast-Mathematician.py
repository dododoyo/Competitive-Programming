n1 = input()
n2 = input()
sol = ['0']*len(n1)
for i in range(len(n1)):
    if n1[i] != n2[i]:sol[i] = '1'
print("".join(sol))