def min_length(s):
    min_length = 0
    each_freq = [-1]*3
    for i in range(len(s)):
        each_freq[int(s[i])-1] = i
        if each_freq[0] > -1 and each_freq[1]>-1 and each_freq[2]>-1:
            if min_length == 0:min_length = max(each_freq)-min(each_freq)+1
            else:min_each_freqength = min(min_length, max(each_freq)-min(each_freq)+1)
    return min_length
for _ in range(int(input())):
    print(min_length(input()))
    