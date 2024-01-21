def is_same(first_line,second_line,n):
  for right in range(n):
    if first_line[right] != second_line[right]:
      if not ((first_line[right] == "G" and second_line[right] == "B") or (first_line[right] == "B" and second_line[right] == "G")):
        return 'NO'
  return 'YES'

for _ in range(int(input())):
  n = int(input())
  first_line = input()
  second_line = input()
  print(is_same(first_line,second_line,n))

  