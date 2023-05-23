#206980924	May/23/2023 21:32	dododoyo	199A - Hexadecimal's theorem	PyPy 3	Accepted	186 ms	0 KB
n = int(input())
'''We are asked to find three numbers 
we know the last two of a fibonnaci number
gives the current fibonacci number so we can
take the last two numbers and make the third one
to be always zero.'''
if n < 2:
    print(0, 0, n)
else:
    a,b = 0,1
    while a+b != n:
        a, b = b, a + b
    print(0, a, b)