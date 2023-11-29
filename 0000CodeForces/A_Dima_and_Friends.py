#brute forces solution
n = int(input())
sum_of_frnds = sum(list(map(int,input().split())))
solution = [1,2,3,4,5]
#the count comes back to dima if remainder is '1'
#so the numbers that make it not back to dima is 
#the ones where if the remainder is differnt from '1'
possibles = [(sum_of_frnds + i)%(n+1) != 1 for i in range(1,6)]
print(sum(possibles))