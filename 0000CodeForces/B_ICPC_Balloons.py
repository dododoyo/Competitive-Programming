#counting + implementation
def solve(n,string):
  char_freq = [0]*26
  offset = ord("A")
  for character in string:
    char_freq[ord(character) - offset] += 1
  solution = 0
  for frequency in char_freq:
    if frequency != 0:
      solution += frequency+1
  return solution

for _ in range(int(input())):
  n = int(input())
  string = input()
  print(solve(n,string))