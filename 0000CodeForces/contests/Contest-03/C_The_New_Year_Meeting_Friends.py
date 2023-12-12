distances = input().split()
distances = [int(i) for i in distances]
print(max(distances)-min(distances))