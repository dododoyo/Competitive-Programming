n = int(input())
soldiers = input().split()
soldiers = [int(i) for i in soldiers]
max_index,min_index,maxsol,minsol = 0,0,soldiers[0],soldiers[0]
#use the for loop to find out where are the min and max are located
for i in range(n):
    if soldiers[i] > maxsol:
        maxsol = soldiers[i]
        max_index = i
    if soldiers[i] <= minsol:
        minsol = soldiers[i]
        min_index = i

#then the number of swaps is the difference between the 
#if the max index is after the min index there will be an 
#overlap when swapping numbers and one swapping will be decreased from both
#but if the max_index is near the begnings there is not overlapping swap
if min_index > max_index:
    print(max_index + (n-min_index-1))
else:
    print(max_index + (n-min_index-2))