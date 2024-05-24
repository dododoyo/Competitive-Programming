from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = defaultdict(int)
    solution = 0
    for i in range(0, len(arr)-2):
        solution += freq.get((0, arr[i], 1, arr[i+1]), 0)
        solution += freq.get((0, arr[i], 2, arr[i+2]), 0)
        solution += freq.get((1, arr[i+1], 2, arr[i+2]), 0)
        solution -= 3*freq.get((0, arr[i], 1, arr[i+1], 2, arr[i+2]), 0)

        freq[0, arr[i], 1, arr[i+1]] += 1
        freq[0, arr[i], 2, arr[i+2]] += 1
        freq[1, arr[i+1], 2, arr[i+2]] += 1

        freq[0, arr[i], 1, arr[i+1], 2, arr[i+2]] += 1
    print(solution)
