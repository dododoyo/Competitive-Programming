l,r=map(int,input().split())

# If the first one is even 
# then the first and the last number 
# can have a common divider of two not one 
# this will disprove the theorem 

# let's make sure the first number is even
while(l%2):
	l+=1
	
# if the range between left and right is not 
	#three we have no solution
if(l+2>r):
	print(-1)
	
# solution can be three consecutive numbers 
else:
	print(l,l+1,l+2)