#time limit exceeded on test18 do with c++
n,k,x = map(int,input().split())
studs = sorted(list(map(int,input().split())))
diff=[]
ans=1
for i in range(1,n):
	if studs[i]-studs[i-1]>x :
		ans+=1
		diff.append((studs[i]-studs[i-1]-1)//x)
diff.sort()
for i in diff :
	if k>=i:
		k-=(i)
		ans-=1
	else:
		break
print(ans)
