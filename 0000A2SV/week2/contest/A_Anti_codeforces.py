for _ in range(int(input())):
  difference = 0
  current_string = input()
  for i in range(10):
    if current_string[i] != 'codeforces'[i]:
      difference += 1
  print(difference)
  