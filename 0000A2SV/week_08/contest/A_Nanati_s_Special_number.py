# find out the position of the largest character in a string with it's ascii value 
for _ in range(int(input())):
  n = int(input())
  s = input()
  max_char = 0
  for char in s:
    max_char = max(ord(char),max_char)
  print(max_char-96)