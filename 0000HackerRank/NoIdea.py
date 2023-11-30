n, m = input().split( )
arr = input().split()
a =set(input().split()) 
b =set(input().split())  
happiness = 0
for num in arr:
    if num in a:
        happiness+=1
    if num in b:
        happiness -=1
print(happiness)
