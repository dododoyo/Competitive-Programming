'''
A story is called interesting if there exists a letter which occurs among all words of the story more times than all other letters together.
'''
def count_freq(word):
  freq = [0]*5
  for char in word:
    freq[ord(char)-97] += 1
  return freq

for _ in range(int(input())):
  n = int(input())
  words = [input() for i in range(n)]
  words.sort(key=lambda x:-max(count_freq(x)))
  print(words)
  
