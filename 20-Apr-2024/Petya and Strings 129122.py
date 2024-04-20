# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

s1 = input().lower()
s2 = input().lower()
for i in range(len(s2)):
    if s1[i] > s2[i]:
        print('1');exit()
    elif s1[i] < s2[i]:
        print('-1');exit()
print('0')