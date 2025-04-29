from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


n,m = ls()
arr1 = ls()
arr2 = ls()

index1,index2 = 0,0
count = 0

while index1 < n and index2 < m:
    if arr1[index1] == arr2[index2]:
        num1_freq = 1
        index1 += 1
        # count num1 frequency if we have multiple
        while index1 < n and arr1[index1] == arr1[index1 - 1]:
            num1_freq += 1
            index1 += 1

        num2_freq = 1
        index2 += 1
        # count num2 frequency if we have multiple
        while index2 < m and arr2[index2] == arr2[index2 - 1]:
            num2_freq += 1
            index2 += 1

        count += num1_freq * num2_freq

    elif arr1[index1] < arr2[index2]:
        index1 += 1
    else:
        index2 += 1

print(count)