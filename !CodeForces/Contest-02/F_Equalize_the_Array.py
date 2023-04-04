from collections import defaultdict
t = int(input())
for i in range(t):
    n = int(input().strip())
    arr = list(map(int,input().split()))
    each_freq = defaultdict(int)
    for i in arr:each_freq[i] += 1
    freq_list = list(each_freq.values())
    freq_list.sort()
    solution = float('inf')
    for i in range(len(freq_list)):
        solution = min(solution,n-(freq_list[i]*(len(freq_list)-i)))
    print(solution)