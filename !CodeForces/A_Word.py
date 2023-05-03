s = input()
upper,lower = 0,0
#count the number of upper and lower cases in the letter
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
#convert letter to uppercase if upper > lower else convert to lowercase 
if upper > lower:
    print(s.upper())        
else:
    print(s.lower())