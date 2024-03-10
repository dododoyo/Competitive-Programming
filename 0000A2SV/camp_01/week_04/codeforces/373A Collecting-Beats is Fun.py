k=int(input())*2
s=''.join(input() for _ in range(4))
if max(s.count(c) for c in '0123456789')>k:
    print ('NO')
else:
    print('YES')
