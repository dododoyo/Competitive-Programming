from collections import defaultdict
t  = int(input())
each_freq = defaultdict(int)
def isPali(strng):
    return strng[::-1] == strng

for i in range(t):
    s,all_a = input(),True
    for i in s:
        if i != 'a':
            all_a = False
    if all_a:
        print('NO')
    else:
        if not isPali('a'+s):
            print('YES')
            print('a'+s)
        else:
            print('YES')
            print(s+'a')

