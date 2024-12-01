from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]



n = ls()[0]
word = input()
char_freq = [0]*26

for x in word:
  char_freq[ord(x.lower())-ord("a")] += 1

solution = "YES"
for i in range(26):
  if not char_freq[i]:
    solution = "NO"
    break

print(solution)
