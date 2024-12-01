from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

n = ls()[0]
file_size = ls()[0]

flash_drives = []
for _ in range(n):
  flash_drives.append(ls()[0])

flash_drives.sort(reverse=True)
count = 0

while file_size > 0:
  file_size -= flash_drives[count]
  count += 1

print(count)
