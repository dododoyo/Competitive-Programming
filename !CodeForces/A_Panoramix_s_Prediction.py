def isPrime(nmbr):
    cont,dvsr = 0,nmbr
    while(dvsr > 0):
        if nmbr % dvsr == 0:cont += 1
        dvsr -= 1
    return cont == 2
def findPrime(numbr):
    while True:
        if isPrime(numbr):
            return numbr
        else:
            numbr += 1
n_and_m = input().split()
print('YES') if findPrime(int(n_and_m[0])+1) == int(n_and_m[1])else print('NO')