import collections
words = collections.defaultdict(int)
n = int(input())
for i in range(n):
    each_team = input()
    words[each_team] +=1
keys = list(words.keys())
if len(keys) == 1:
    print(keys[0])
else:
    print(keys[0]) if words[keys[0]] > words[keys[1]] else print(keys[1])