""" For every good cell, DZY wants to put a chessman on it.
"." means cell is good, while a "-" means it is bad."""

n,m = map(int,input().split())
for i in range(n):
	# read line 
	s=list(input())
	for j in range(m):
		"""if current cell is good write on it based on 
		any two adjacent cells will always have one even 
		and one odd sum of indices, ensuring that no two 
		chessmen of the same color are on adjacent cells."""
		if s[j]=='.':
			if (i+j)%2:
				s[j] = "B"
			else:
				s[j] = "W"
	print(''.join(s))

