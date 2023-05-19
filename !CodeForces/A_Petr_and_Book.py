pages = int(input())
each_day_read = list(map(int,input().split()))
i,total_read = 0,0
while i < 7:
    total_read += each_day_read[i]
    if total_read >= pages:
        print(i+1);exit()
    i+=1
    if i == 7:i=0
    
