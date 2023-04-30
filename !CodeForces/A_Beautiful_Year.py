year = int(input())
while True:
    year+=1
    a = year%10;b = int((year/10))%10;c =int((year/100))%10;d=int((year/1000))%10
    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:break;
print(year)