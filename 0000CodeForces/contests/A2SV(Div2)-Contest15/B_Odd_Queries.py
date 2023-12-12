# for _ in range(int(input())):
# 	#second approach
# 	n, q = map(int, input().split())
# 	arr = input().split()
# 	pref = [0] * (n+1)
# 	for i in range(1, n+1):
# 		pref[i] = pref[i-1] + int(arr[i-1])

# 	for i in range(q):
# 		l, r, k = map(int, input().split())
# 		ans = pref[n] + pref[r] - pref[l-1] + k*(r-l+1)
		
# 		print('YES' if ans % 2 == 1 else 'NO')

# t = int(input())

# for _ in range(t):
# 	n, q = map(int, input().split())
# 	a = input().split()
# 	pref = [0] * (n+1)
	
# 	for i in range(1, n+1):
# 		pref[i] = pref[i-1] + int(a[i-1])
		
#   l,r,k = map(int, input().split())

# 	for i in range(q):
# 		ans = pref[n] + pref[r] - pref[l-1] + k*(r-l+1)
# 		print('YES' if ans % 2 == 1 else 'NO')

t = int(input())

for _ in range(t):
    n,q = map(int, input().split())
    a = input().split()
    pref = [0] * (n+1)
    
    for i in range(1, n+1):
        pref[i] = pref[i-1] + int(a[i-1])
        
    

    for i in range(q):
        l,r,k = map(int, input().split())
        ans = pref[n] + pref[r] - pref[l-1] + k*(r-l+1)
        print('YES' if ans % 2 == 1 else 'NO')
