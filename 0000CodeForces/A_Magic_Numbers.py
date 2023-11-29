n=input()

"""
for the number to be a magic number 
first, It must consist of only 1's and 4's
second, the number must start with 1 as it 
can't with four because the building blocks 
also start with 1.
third, it must not contain "444"
"""
if (len(n)==n.count('4')+n.count('1')) and (n[0]=='1') and ('444' not in n):
	print('YES')
else:
	print('NO')

