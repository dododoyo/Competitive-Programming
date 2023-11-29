areas = list(map(int,input().split()))
#formula provided after some 
# manipulation for each sides
side1 = ((areas[0]*areas[1])/areas[2])**0.5
side2 = ((areas[0]*areas[2])/areas[1])**0.5
side3 = ((areas[1]*areas[2])/areas[0])**0.5
print(int(4*(side1+side2+side3)))