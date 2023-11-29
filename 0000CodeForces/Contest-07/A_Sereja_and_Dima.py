def find_points():
    n=int(input())
    cards=list(map(int,input().split()))
    dima=serja=0
    for i in range(n):
        current_max=max(cards[0],cards[-1])
        if i%2==0:serja+=current_max
        else:dima+=current_max
        #we can remove with value because they are distinct
        cards.remove(current_max)
    print(serja,dima)
find_points()