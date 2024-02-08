n = int(input())
points,center_points = [0]*n,0
for i in range(n):points[i] = list(map(int,input().split()))

#brute_force approach 
for point1 in points:
    right,left,up,down = 0,0,0,0
    for point2 in points:
        if point1 != point2:
            # if the points have the same x value depending
            # on the y value either one is on top
            # of or below the other or the same y axis
            if point1[0] == point2[0]:
                if point1[1] <  point2[1]: down += 1
                elif point1[1] > point2[1]: up += 1
            # if the points have the same y value 
            # either one is left of or right of the 
            # other or the same x axis
            if point1[1] == point2[1]:
                if point1[0] <  point2[0]: left += 1
                elif point1[0] > point2[0]: right += 1
    if (right and left and up and down): center_points += 1
print(center_points)