t = int(input())
for _ in range(t):
    rgb = input().split()
    rgb = [int(i) for i in rgb]
    rgb.sort()
    how_diff = rgb[2] - rgb[1]
    remain = min(how_diff, rgb[0])
    rgb[0] -= remain
    rgb[1] += remain
    rgb[1] += rgb[0]//2
    rgb[2] += rgb[0]//2
    ans = min(rgb[1], rgb[2])
    print(ans)
