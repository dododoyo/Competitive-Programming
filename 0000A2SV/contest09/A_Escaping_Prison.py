for _ in range(int(input())):
    n, h = map(int, input().split())
    blancket_height = 0
    for i in range(n):
        w, l = map(int, input().split())
        blancket_height += max(w,l)
    print("NO" if blancket_height < h else "YES")